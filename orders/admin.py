from django.contrib import admin
from django.utils.html import format_html

from .models import Order, OrderItem, ShippingMethod



# ==========================================
# ORDER ITEMS INLINE
# ==========================================

class OrderItemInline(admin.TabularInline):

    model = OrderItem

    extra = 0

    readonly_fields = (
        "product",
        "quantity",
        "price",
        "item_total",
    )


    def item_total(self, obj):

        if obj.price is None:
            return "0.00 €"

        return obj.quantity * obj.price


    item_total.short_description = "Total"



# ==========================================
# ORDER ADMIN
# ==========================================

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):


    list_display = (
        "order_number",
        "email",
        "first_name",
        "last_name",
        "total_price",
        "shipping_method",
        "status_colored",
        "created",
    )


    list_filter = (
        "status",
        "shipping_method",
        "created",
    )


    search_fields = (
        "email",
        "first_name",
        "last_name",
    )


    readonly_fields = (
        "created",
        "user",
        "total_price",
    )


    fieldsets = (

        (
            "Customer information",
            {
                "fields": (
                    "user",
                    "email",
                    "first_name",
                    "last_name",
                )
            }
        ),


        (
            "Shipping address",
            {
                "fields": (
                    "address",
                    "city",
                    "country",
                )
            }
        ),


        (
            "Shipping",
            {
                "fields": (
                    "shipping_method",
                    "shipping_price",
                    "carrier",
                    "tracking_number",
                )
            }
        ),


        (
            "Order information",
            {
                "fields": (
                    "status",
                    "payment_method",
                    "total_price",
                    "created",
                )
            }
        ),

    )


    inlines = [
        OrderItemInline,
    ]


    # Rýchle akcie na zmenu statusu
    actions = ["mark_as_paid", "mark_as_shipped", "mark_as_delivered"]
    
    def mark_as_paid(self, request, queryset):
        queryset.update(status="paid")
    mark_as_paid.short_description = "✅ Mark selected as PAID"
    
    def mark_as_shipped(self, request, queryset):
        queryset.update(status="shipped")
    mark_as_shipped.short_description = "📦 Mark selected as SHIPPED"
    
    def mark_as_delivered(self, request, queryset):
        queryset.update(status="delivered")
    mark_as_delivered.short_description = "🏠 Mark selected as DELIVERED"


    # Farebné statusy
    def status_colored(self, obj):
        colors = {
            "pending": "orange",
            "paid": "blue",
            "processing": "purple",
            "shipped": "green",
            "delivered": "darkgreen",
            "cancelled": "red",
        }
        color = colors.get(obj.status, "black")
        status_display = obj.get_status_display() if hasattr(obj, 'get_status_display') else obj.status
        return format_html(
            '<span style="color: {}; font-weight: bold;">{}</span>',
            color,
            status_display
        )
    status_colored.short_description = "Status"



# ==========================================
# SHIPPING METHOD ADMIN
# ==========================================

@admin.register(ShippingMethod)
class ShippingMethodAdmin(admin.ModelAdmin):
    list_display = ("logo", "name", "price", "is_active", "sort_order")
    list_filter = ("is_active",)
    list_editable = ("price", "is_active", "sort_order")