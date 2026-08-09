from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _
import re
from orders.models import Order
from custom_orders.models import CustomOrder
from wishlist.models import Wishlist
from reviews.models import Review


# REGISTER
def register(request):

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        # Validácia
        if User.objects.filter(username=username).exists():
            messages.error(request, _("Username already exists"))
            return render(request, "accounts/register.html")

        if len(username) < 3:
            messages.error(request, _("Username must be at least 3 characters"))
            return render(request, "accounts/register.html")

        if password != password2:
            messages.error(request, _("Passwords do not match"))
            return render(request, "accounts/register.html")

        if len(password) < 8:
            messages.error(request, _("Password must be at least 8 characters"))
            return render(request, "accounts/register.html")

        if not re.search(r'[A-Z]', password):
            messages.error(request, _("Password must contain at least one uppercase letter"))
            return render(request, "accounts/register.html")

        if not re.search(r'[0-9]', password):
            messages.error(request, _("Password must contain at least one number"))
            return render(request, "accounts/register.html")


        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        login(request, user)
        messages.success(request, _("Account created successfully!"))

        return redirect("home")


    return render(request, "accounts/register.html")


# LOGIN
def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, _("Invalid username or password"))


    return render(request, "accounts/login.html")


# PROFILE

@login_required
def profile(request):

    orders = Order.objects.filter(user=request.user).order_by("-created")
    custom_orders = CustomOrder.objects.filter(user=request.user).order_by("-created")

    orders_count = orders.count()
    wishlist_count = Wishlist.objects.filter(user=request.user).count()
    reviews_count = Review.objects.filter(user=request.user).count()

    return render(
        request,
        "accounts/profile.html",
        {
            "orders": orders,
            "custom_orders": custom_orders,
            "orders_count": orders_count,
            "wishlist_count": wishlist_count,
            "reviews_count": reviews_count,
        }
    )


@login_required
def update_profile(request):
    if request.method == "POST":
        user = request.user
        user.email = request.POST.get("email", user.email)
        user.first_name = request.POST.get("first_name", user.first_name)
        user.last_name = request.POST.get("last_name", user.last_name)
        user.save()
        messages.success(request, _("Profile updated successfully!"))
    return redirect("profile")


# LOGOUT

def logout_view(request):

    logout(request)
    return redirect("home")