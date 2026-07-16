from django.urls import path
from . import views


urlpatterns = [

    path(
        "",
        views.shop,
        name="shop"
    ),


    path(
        "product/<slug:slug>/",
        views.product_detail,
        name="product_detail"
    ),


    path(
        "dashboard/",
        views.admin_dashboard,
        name="admin_dashboard"
    ),


    path(
        "dashboard/products/",
        views.admin_products,
        name="admin_products"
    ),


    path(
        "dashboard/products/edit/<int:product_id>/",
        views.edit_product,
        name="edit_product"
    ),

    path(
        "dashboard/products/delete/<int:product_id>/",
        views.delete_product,
        name="delete_product"
    ),
    path(
        "dashboard/products/add/",
        views.add_product,
        name="add_product"
    ),

    path(
    "dashboard/products/<int:product_id>/gallery/",
    views.product_gallery,
    name="product_gallery"
),

]