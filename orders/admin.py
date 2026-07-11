from django.contrib import admin

from .models import Order, OrderItem



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
    "status",
    "created",
)


    list_filter = (
        "status",
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
            "Order information",
            {
                "fields": (
                    "status",
                    "total_price",
                    "created",
                )
            }
        ),

    )


    inlines = [
        OrderItemInline,
    ]