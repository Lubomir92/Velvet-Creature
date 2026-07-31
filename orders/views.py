from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.urls import reverse
from cart.views import get_cart_data
from .email import send_order_email
from .forms import ShippingForm
from decimal import Decimal
import stripe
import resend
import os

from .models import Order, OrderItem, ShippingMethod
from .invoice import generate_invoice, generate_invoice_bytes
from products.models import Product


stripe.api_key = settings.STRIPE_SECRET_KEY



# ==================================================
# CHECKOUT
# ==================================================

def checkout(request):

    cart = request.session.get("cart", {})

    if not cart:
        return redirect("cart_detail")

    products = []
    subtotal = 0

    for product_id, qty in cart.items():
        product = get_object_or_404(Product, id=product_id)

        if qty > product.stock:
            return render(
                request,
                "cart/cart_detail.html",
                {
                    "error": f"Only {product.stock} pieces available for {product.name}",
                    **get_cart_data(request)
                }
            )

        subtotal += product.price * qty
        products.append({
            "product": product,
            "qty": qty
        })

    shipping_methods = ShippingMethod.objects.filter(is_active=True)
    
    if request.method == "POST":
        
        # DOPRAVA JE POVINNÁ!
        shipping_id = request.POST.get("shipping_method")
        if not shipping_id:
            return render(request, "orders/checkout.html", {
                "error": "Veuillez sélectionner un mode de livraison.",
                "subtotal": subtotal,
                "shipping_price": Decimal("0"),
                "total": subtotal,
                "items": products,
                "shipping_methods": shipping_methods,
            })
        
        shipping_price = Decimal("0")
        if shipping_id:
            try:
                shipping = ShippingMethod.objects.get(id=shipping_id)
                shipping_price = shipping.price
            except:
                pass

        payment_method = request.POST.get("payment_method", "card")

        order = Order.objects.create(
            user=request.user if request.user.is_authenticated else None,
            email=request.POST.get("email"),
            first_name=request.POST.get("first_name"),
            last_name=request.POST.get("last_name"),
            address=request.POST.get("address"),
            city=request.POST.get("city"),
            country=request.POST.get("country"),
            phone=request.POST.get("phone", ""),
            postal_code=request.POST.get("postal_code", ""),
            note=request.POST.get("note", ""),
            shipping_method_id=shipping_id if shipping_id else None,
            shipping_price=shipping_price,
            total_price=subtotal + shipping_price,
            payment_method=payment_method,
            status="pending"
        )

        for item in products:
            OrderItem.objects.create(
                order=order,
                product=item["product"],
                quantity=item["qty"],
                price=item["product"].price
            )

        request.session["last_order_id"] = order.id

        # BANKOVÝ PREVOD
        if payment_method == "bank_transfer":
            request.session["cart"] = {}
            return redirect("payment_success")

        # PLATBA KARTOU
        else:
            session = stripe.checkout.Session.create(
                customer_email=order.email,
                payment_method_types=["card"],
                mode="payment",
                line_items=[{
                    "price_data": {
                        "currency": "eur",
                        "product_data": {
                            "name": f"Velvet Creature Order #{order.id}"
                        },
                        "unit_amount": int(order.total_price * 100),
                    },
                    "quantity": 1,
                }],
                metadata={
                    "order_id": order.id
                },
                success_url=request.build_absolute_uri(
                    reverse("payment_success")
                ),
                cancel_url=request.build_absolute_uri(
                    reverse("payment_cancel")
                ),
            )

            return redirect(session.url)

    # GET request
    shipping_price = Decimal("0")
    if shipping_methods.exists():
        shipping_price = shipping_methods.first().price

    return render(
        request,
        "orders/checkout.html",
        {
            "subtotal": subtotal,
            "shipping_price": shipping_price,
            "total": subtotal + shipping_price,
            "items": products,
            "shipping_methods": shipping_methods,
        }
    )
# ==================================================
# USER ORDERS
# ==================================================

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user).order_by("-created")
    return render(request, "orders/order_list.html", {"orders": orders})


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, "orders/order_detail.html", {"order": order})


# ==================================================
# ADMIN
# ==================================================

@staff_member_required
def admin_orders(request):
    orders = Order.objects.all().order_by("-created")
    return render(request, "orders/admin_orders.html", {"orders": orders})


@staff_member_required
def mark_paid(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = "paid"
    order.save()
    send_order_email(order, "Your payment was received", "emails/paid_email.html")
    return redirect("admin_orders")


@staff_member_required
def mark_processing(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = "processing"
    order.save()
    send_order_email(order, "Your order is being prepared", "emails/processing_email.html")
    return redirect("admin_orders")


@staff_member_required
def mark_shipped(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == "POST":
        form = ShippingForm(request.POST, instance=order)
        if form.is_valid():
            order = form.save()
            order.status = "shipped"
            order.save()
            send_order_email(order, "Your order has been shipped", "emails/shipped_email.html")
            return redirect("admin_orders")
    else:
        form = ShippingForm(instance=order)
    return render(request, "orders/shipping.html", {"form": form, "order": order})


@staff_member_required
def mark_delivered(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = "delivered"
    order.save()
    send_order_email(order, "Your order has been delivered", "emails/delivered_email.html")
    return redirect("admin_orders")


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, "orders/admin_order_detail.html", {"order": order})


# ==================================================
# STRIPE SUCCESS / CANCEL
# ==================================================

def payment_success(request):
    order = None
    order_id = request.session.get("last_order_id")

    if order_id:
        try:
            order = Order.objects.get(id=order_id)
            if not order.stock_updated:
                for item in order.items.all():
                    item.product.stock -= item.quantity
                    item.product.save()
                order.stock_updated = True
                order.save()

            # Resend API email - zákazníkovi
            try:
                html_message = render_to_string("emails/order_confirmation.html", {"order": order})
                resend.api_key = os.getenv("RESEND_API_KEY")
                resend.Emails.send({
                    "from": "Velvet Creature <onboarding@resend.dev>",
                    "to": [order.email],
                    "subject": f"Velvet Creature - Order #{order.order_number}",
                    "html": html_message,
                })
                
                # Admin notifikácia
                resend.Emails.send({
                    "from": "Velvet Creature <onboarding@resend.dev>",
                    "to": ["lubma3D@outlook.fr"],
                    "subject": f"🔔 Nouvelle commande #{order.order_number}",
                    "html": f"""
                    <h2>Nouvelle commande!</h2>
                    <p><strong>Numéro:</strong> {order.order_number}</p>
                    <p><strong>Client:</strong> {order.first_name} {order.last_name}</p>
                    <p><strong>Email:</strong> {order.email}</p>
                    <p><strong>Téléphone:</strong> {order.phone}</p>
                    <p><strong>Total:</strong> €{order.total_price}</p>
                    <p><strong>Paiement:</strong> {order.payment_method}</p>
                    <p><strong>Adresse:</strong> {order.address}, {order.postal_code} {order.city}, {order.country}</p>
                    <p><strong>Note:</strong> {order.note}</p>
                    <p><a href="https://www.velvetcreature.fr/fr/orders/admin/">Voir les commandes</a></p>
                    """,
                })
            except:
                pass

        except Order.DoesNotExist:
            pass

        request.session["cart"] = {}
        request.session.pop("last_order_id", None)

    return render(request, "orders/payment_success.html", {"order": order})


def payment_cancel(request):
    return render(request, "orders/payment_cancel.html")


# ==================================================
# STRIPE WEBHOOK
# ==================================================

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE")
    try:
        event = stripe.Webhook.construct_event(payload, sig_header, settings.STRIPE_WEBHOOK_SECRET)
    except Exception:
        return HttpResponse(status=400)

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        order_id = session["metadata"]["order_id"]
        try:
            order = Order.objects.get(id=order_id)
            order.status = "paid"
            order.save()
            for item in order.items.all():
                item.product.stock -= item.quantity
                item.product.save()
        except Order.DoesNotExist:
            pass

    return HttpResponse(status=200)


# ==================================================
# PDF INVOICE
# ==================================================

@login_required
def invoice(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return generate_invoice(order)