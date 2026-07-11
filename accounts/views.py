from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from orders.models import Order
from custom_orders.models import CustomOrder




# REGISTER
def register(request):

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")


        if User.objects.filter(username=username).exists():

            messages.error(request, "Používateľ už existuje")

            return redirect("register")


        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )


        login(request, user)

        return redirect("home")


    return render(request, "accounts/register.html")




# LOGIN
def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")


        user = authenticate(
            request,
            username=username,
            password=password
        )


        if user is not None:

            login(request, user)

            return redirect("home")


        else:

            messages.error(
                request,
                "Zlé meno alebo heslo"
            )


    return render(request, "accounts/login.html")




# PROFILE

@login_required
def profile(request):

    orders = Order.objects.filter(
        user=request.user
    ).order_by("-created")


    custom_orders = CustomOrder.objects.filter(
        user=request.user
    ).order_by("-created")


    return render(
        request,
        "accounts/profile.html",
        {
            "orders": orders,
            "custom_orders": custom_orders,
        }
    )


# LOGOUT

def logout_view(request):

    logout(request)

    return redirect("home")