from django.urls import path
from . import views

urlpatterns = [
    path("checkout/", views.checkout, name="checkout"),

    
    path("list/", views.order_list, name="order_list"),
    path("<int:order_id>/", views.order_detail, name="order_detail"),

    path("admin/", views.admin_orders, name="admin_orders"),
    path("admin/<int:order_id>/paid/", views.mark_paid, name="mark_paid"),
    path("admin/<int:order_id>/shipped/", views.mark_shipped, name="mark_shipped"),

    path("success/", views.payment_success, name="payment_success"),
    path("cancel/", views.payment_cancel, name="payment_cancel"),

    path("webhook/", views.stripe_webhook, name="stripe_webhook"),
]