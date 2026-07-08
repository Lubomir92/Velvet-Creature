from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import stripe

from .models import Order, OrderItem
from products.models import Product

stripe.api_key = settings.STRIPE_SECRET_KEY


# ---------------- CHECKOUT ----------------

@login_required
def checkout(request):
    cart = request.session.get("cart", {})

    if not cart:
        return redirect("cart_detail")

    products = []
    total = 0

    for product_id, qty in cart.items():
        product = get_object_or_404(Product, id=product_id)
        total += product.price * qty
        products.append({"product": product, "qty": qty})

    if request.method == "POST":

        order = Order.objects.create(
            user=request.user,
            total_price=total,
            status="pending"
        )

        for item in products:
            OrderItem.objects.create(
                order=order,
                product=item["product"],
                quantity=item["qty"],
                price=item["product"].price
            )

        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            mode="payment",

            line_items=[{
                "price_data": {
                    "currency": "eur",
                    "product_data": {
                        "name": f"Velvet Creature Order #{order.id}",
                    },
                    "unit_amount": int(total * 100),
                },
                "quantity": 1,
            }],

            metadata={
                "order_id": order.id
            },

            success_url=request.build_absolute_uri("/orders/success/"),
            cancel_url=request.build_absolute_uri("/orders/cancel/"),
        )

        request.session["cart"] = {}

        return redirect(session.url)

    return render(request, "orders/checkout.html", {
        "total": total,
        "items": products
    })


# ---------------- ORDERS ----------------

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user).order_by("-created")
    return render(request, "orders/order_list.html", {"orders": orders})


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, "orders/order_detail.html", {"order": order})


# ---------------- ADMIN ----------------

@staff_member_required
def admin_orders(request):
    orders = Order.objects.all().order_by("-created")
    return render(request, "orders/admin_orders.html", {"orders": orders})


@staff_member_required
def mark_paid(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = "paid"
    order.save()
    return redirect("admin_orders")


@staff_member_required
def mark_shipped(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = "shipped"
    order.save()
    return redirect("admin_orders")


# ---------------- STRIPE ----------------

@login_required
def payment_success(request):
    return render(request, "orders/payment_success.html")


@login_required
def payment_cancel(request):
    return render(request, "orders/payment_cancel.html")


# ---------------- WEBHOOK (ONLY ONCE!) ----------------

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE")

    try:
        event = stripe.Webhook.construct_event(
            payload,
            sig_header,
            settings.STRIPE_WEBHOOK_SECRET
        )
    except Exception:
        return HttpResponse(status=400)

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        order_id = session["metadata"]["order_id"]

        try:
            order = Order.objects.get(id=order_id)
            order.status = "paid"
            order.save()
        except Order.DoesNotExist:
            pass

    return HttpResponse(status=200)