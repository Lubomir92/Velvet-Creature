from django.shortcuts import render, get_object_or_404
from .models import Product


def shop(request):
    products = Product.objects.all().order_by("-created")
    return render(request, "products/shop.html", {
        "products": products
    })


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "products/detail.html", {
        "product": product
    })