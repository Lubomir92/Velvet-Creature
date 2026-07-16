from django.urls import path
from . import views


urlpatterns = [

    # ==========================
    # CHECKOUT
    # ==========================

    path(
        "checkout/",
        views.checkout,
        name="checkout"
    ),


    # ==========================
    # PAYMENT SUCCESS / CANCEL
    # ==========================

    path(
        "success/",
        views.payment_success,
        name="payment_success"
    ),


    path(
        "cancel/",
        views.payment_cancel,
        name="payment_cancel"
    ),



    # ==========================
    # INVOICE PDF
    # ==========================

    path(
        "invoice/<int:order_id>/",
        views.invoice,
        name="invoice"
    ),



    # ==========================
    # USER ORDERS
    # ==========================

    path(
        "list/",
        views.order_list,
        name="order_list"
    ),

path(
    "admin/<int:order_id>/",
    views.admin_order_detail,
    name="admin_order_detail"
),
    path(
        "<int:order_id>/",
        views.order_detail,
        name="order_detail"
    ),



    # ==========================
    # ADMIN ORDERS
    # ==========================

    path(
        "admin/",
        views.admin_orders,
        name="admin_orders"
    ),


    path(
        "admin/<int:order_id>/paid/",
        views.mark_paid,
        name="mark_paid"
    ),

    path(
    "admin/<int:order_id>/processing/",
    views.mark_processing,
    name="mark_processing"
),

    path(
    "admin/<int:order_id>/delivered/",
    views.mark_delivered,
    name="mark_delivered"
),

    path(
    "admin/<int:order_id>/processing/",
    views.mark_processing,
    name="mark_processing"
),
   
    path(
        "admin/<int:order_id>/shipped/",
        views.mark_shipped,
        name="mark_shipped"
    ),



    # ==========================
    # STRIPE WEBHOOK
    # ==========================

    path(
        "webhook/",
        views.stripe_webhook,
        name="stripe_webhook"
    ),

]