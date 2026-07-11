from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import CustomOrder
from .forms import CustomOrderForm

from .emails import (
    send_custom_order_received_email,
    send_admin_new_custom_order_email,
)



# ==================================================
# CREATE CUSTOM ORDER
# ==================================================

def custom_order_create(request):


    if request.method == "POST":


        form = CustomOrderForm(

            request.POST,

            request.FILES

        )



        if form.is_valid():


            order = form.save(commit=False)



            if request.user.is_authenticated:

                order.user = request.user



            order.save()



            # EMAIL TO CUSTOMER

            send_custom_order_received_email(order)



            # EMAIL TO ADMIN

            send_admin_new_custom_order_email(order)



            return redirect(

                "custom_order_success"

            )



    else:


        form = CustomOrderForm()



    return render(

        request,

        "custom_orders/create.html",

        {
            "form": form
        }

    )





# ==================================================
# SUCCESS PAGE
# ==================================================

def custom_order_success(request):


    return render(

        request,

        "custom_orders/success.html"

    )





# ==================================================
# CUSTOMER CUSTOM ORDER DETAIL
# ==================================================

@login_required
def custom_order_detail(request, order_id):


    custom_order = get_object_or_404(

        CustomOrder,

        id=order_id,

        user=request.user

    )



    return render(

        request,

        "custom_orders/detail.html",

        {
            "custom_order": custom_order
        }

    )