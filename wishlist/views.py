from django.shortcuts import redirect, render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from products.models import Product
from .models import Wishlist



# ==========================================
# ADD / REMOVE WISHLIST
# ==========================================

@login_required
def toggle_wishlist(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    wishlist_item = Wishlist.objects.filter(
        user=request.user,
        product=product
    ).first()

    if wishlist_item:

        wishlist_item.delete()

        added = False

    else:

        Wishlist.objects.create(
            user=request.user,
            product=product
        )

        added = True

    return JsonResponse({

        "success": True,
        "added": added,

    })





# ==========================================
# MY WISHLIST
# ==========================================

@login_required
def wishlist_page(request):

    items = Wishlist.objects.filter(
        user=request.user
    ).select_related(
        "product"
    ).order_by(
        "-created"
    )


    return render(
        request,
        "wishlist/wishlist.html",
        {
            "items": items
        }
    )