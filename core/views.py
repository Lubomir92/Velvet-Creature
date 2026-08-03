from django.shortcuts import render, redirect
from products.models import Product


def home(request):
    # Presmerovanie na francúzsku verziu
    return redirect('/fr/')


def about(request):
    return render(
        request,
        "about.html"
    )