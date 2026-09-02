from django.shortcuts import render
from products.models import Product
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .chatbot import get_bot_response


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

def about(request):
    return render(
        request,
        "about.html"
    )
def legal(request):
    return render(request, "legal.html")

@csrf_exempt
def chatbot_api(request):
    if request.method == "POST":
        import json
        data = json.loads(request.body)
        message = data.get("message", "")
        language = data.get("language", "fr")
        response = get_bot_response(message, language)
        return JsonResponse({"response": response})
    return JsonResponse({"error": "POST only"}, status=400)