from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from products.models import Product



# ==================================================
# HELPER - BUILD CART DATA
# ==================================================

def get_cart_data(request):

    cart = request.session.get("cart", {})

    cart_items = []
    cart_total = 0
    cart_count = 0


    for product_id, quantity in cart.items():

        product = get_object_or_404(
            Product,
            id=product_id
        )


        item_total = product.price * quantity


        cart_items.append({

            "product": product,

            "quantity": quantity,

            "total_price": item_total

        })


        cart_total += item_total

        cart_count += quantity



    return {
        "cart_items": cart_items,
        "cart_total": cart_total,
        "cart_count": cart_count
    }




# ==================================================
# ADD TO CART
# ==================================================

def add_to_cart(request, product_id):

    cart = request.session.get("cart", {})


    product_id = str(product_id)


    cart[product_id] = cart.get(product_id, 0) + 1


    request.session["cart"] = cart

    request.session.modified = True



    data = get_cart_data(request)


    return JsonResponse({

        "success": True,

        "cart_count": data["cart_count"],

        "cart_total": float(data["cart_total"])

    })





# ==================================================
# CART DETAIL PAGE
# ==================================================

def cart_detail(request):

    data = get_cart_data(request)


    return render(
        request,
        "cart/cart_detail.html",
        data
    )





# ==================================================
# INCREASE QTY
# ==================================================

def increase_qty(request, product_id):

    cart = request.session.get("cart", {})

    product_id = str(product_id)


    if product_id in cart:

        product = get_object_or_404(
            Product,
            id=product_id
        )


        if cart[product_id] < product.stock:

            cart[product_id] += 1


        else:

            return JsonResponse({

                "success": False,

                "message": f"Only {product.stock} pieces available",

                "cart_count": sum(cart.values())

            })



    request.session["cart"] = cart

    request.session.modified = True


    data = get_cart_data(request)



    return JsonResponse({

        "success": True,

        "cart_count": data["cart_count"],

        "cart_total": float(data["cart_total"])

    })





# ==================================================
# DECREASE QTY
# ==================================================

def decrease_qty(request, product_id):

    cart = request.session.get("cart", {})


    product_id = str(product_id)


    if product_id in cart:


        cart[product_id] -= 1



        if cart[product_id] <= 0:

            del cart[product_id]



    request.session["cart"] = cart

    request.session.modified = True



    data = get_cart_data(request)



    return JsonResponse({

        "success": True,

        "cart_count": data["cart_count"],

        "cart_total": float(data["cart_total"])

    })





# ==================================================
# REMOVE ITEM
# ==================================================

def remove_from_cart(request, product_id):

    cart = request.session.get("cart", {})


    product_id = str(product_id)


    if product_id in cart:

        del cart[product_id]



    request.session["cart"] = cart

    request.session.modified = True



    data = get_cart_data(request)



    return JsonResponse({

        "success": True,

        "cart_count": data["cart_count"],

        "cart_total": float(data["cart_total"])

    })





# ==================================================
# CHECKOUT
# ==================================================


def checkout(request):

    data = get_cart_data(request)


    return render(
        request,
        "cart/checkout.html",
        data
    )





# ==================================================
# CART DRAWER HTML
# ==================================================

def cart_drawer(request):

    data = get_cart_data(request)


    return render(
        request,
        "cart/cart_drawer.html",
        data
    )





# ==================================================
# CONTEXT PROCESSOR
# ==================================================

def cart_context(request):

    return get_cart_data(request)