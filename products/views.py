from django.shortcuts import render, get_object_or_404
from .models import Product
from wishlist.models import Wishlist


def shop(request):

    products = Product.objects.all()


    wishlist_products = []


    if request.user.is_authenticated:

        wishlist_products = list(
            Wishlist.objects.filter(
                user=request.user
            ).values_list(
                "product_id",
                flat=True
            )
        )



    return render(
        request,
        "products/shop.html",
        {
            "products": products,
            "wishlist_products": wishlist_products
        }
    )



def product_detail(request, id):

    product = get_object_or_404(
        Product,
        id=id
    )

    return render(
        request,
        "products/detail.html",
        {
            "product": product
        }
    )
