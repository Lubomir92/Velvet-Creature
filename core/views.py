from django.shortcuts import render
from products.models import Product


def home(request):

    featured_products = Product.objects.filter(
        featured=True
    ).order_by("-created")[:3]


    return render(
        request,
        "products/home.html",
        {
            "featured_products": featured_products,
        }
    )