from django.contrib import admin
from django.urls import path, include

from django.conf.urls.i18n import i18n_patterns

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path("i18n/", include("django.conf.urls.i18n")),

    path("admin/", admin.site.urls),

]


urlpatterns += i18n_patterns(

    path("", include("core.urls")),

    path("shop/", include("products.urls")),

    path("cart/", include("cart.urls")),

    path("orders/", include("orders.urls")),

    path("accounts/", include("accounts.urls")),

    path("custom/", include("custom_orders.urls")),

)


# ==========================================
# MEDIA (development)
# ==========================================

if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )