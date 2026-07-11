from django.urls import path

from . import views



urlpatterns = [


    path(

        "",

        views.custom_order_create,

        name="custom_order_create"

    ),



    path(

        "success/",

        views.custom_order_success,

        name="custom_order_success"

    ),
    path(
        "<int:order_id>/",
        views.custom_order_detail,
        name="custom_order_detail"
    ),


]
