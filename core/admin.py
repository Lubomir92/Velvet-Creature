from django.contrib import admin
from django.db.models import Sum, Count
from django.utils.html import format_html
from orders.models import Order
from products.models import Product
from custom_orders.models import CustomOrder
from datetime import date, timedelta


class DashboardAdmin(admin.AdminSite):
    pass


# Nahradí predvolený admin panel
# admin.site = DashboardAdmin()