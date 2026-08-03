from django.contrib import admin
from django.urls import path, include

from django.conf.urls.i18n import i18n_patterns

from django.conf import settings
from django.conf.urls.static import static



# ==========================================
# NON LANGUAGE URLS
# ==========================================

urlpatterns = [

    # Language switch
    path(
        "i18n/",
        include("django.conf.urls.i18n")
    ),


    # Django admin
    path(
        "admin/",
        admin.site.urls
    ),

]



# ==========================================
# MAIN WEBSITE URLS
# ==========================================

urlpatterns += i18n_patterns(
   

    # HOME
    path(
        "",
        include("core.urls")
    ),


    # SHOP
    path(
        "shop/",
        include("products.urls")
    ),


    # CART
    path(
        "cart/",
        include("cart.urls")
    ),


    # ORDERS
    path(
        "orders/",
        include("orders.urls")
    ),


    # ACCOUNTS
    path(
        "accounts/",
        include("accounts.urls")
    ),


    # CUSTOM ORDERS
    path(
        "custom/",
        include("custom_orders.urls")
    ),


    # WISHLIST
    path(
        "wishlist/",
        include("wishlist.urls")
    ),


)



# ==========================================
# STATIC & MEDIA FILES
# ==========================================

urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
)

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)