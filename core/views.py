from django.shortcuts import render, redirect
from products.models import Product


def home(request):
    # Presmerovanie na francúzsku verziu
    if not request.path.startswith('/fr/') and not request.path.startswith('/en/') and not request.path.startswith('/sk/'):
        return redirect('/fr/')

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

def about(request):
    return render(
        request,
        "about.html"
    )