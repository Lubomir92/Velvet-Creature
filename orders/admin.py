from django.contrib import admin, messages
from django.utils.html import format_html
from .models import Order, OrderItem
from .email import send_order_email


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['price']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number_colored', 'first_name', 'last_name', 'email', 'status_colored', 'created']
    list_filter = ['status', 'created']
    search_fields = ['first_name', 'last_name', 'email', 'order_number']
    inlines = [OrderItemInline]
    actions = ['send_confirmation_email', 'send_shipped_email']

    def order_number_colored(self, obj):
        return format_html('<strong>{}</strong>', obj.order_number)
    order_number_colored.short_description = 'Order Number'
    order_number_colored.admin_order_field = 'order_number'

    def status_colored(self, obj):
        colors = {
            'pending': 'orange',
            'processing': 'blue',
            'confirmed': 'green',
            'shipped': 'purple',
            'delivered': 'teal',
            'cancelled': 'red',
        }
        color = colors.get(obj.status, 'black')
        return format_html(
            '<span style="color: {}; font-weight: bold;">{}</span>',
            color,
            obj.get_status_display()
        )
    status_colored.short_description = 'Status'
    status_colored.admin_order_field = 'status'

    def save_model(self, request, obj, form, change):
        print(f"DEBUG save_model: change={change}, status={obj.status}")
        if change:
            try:
                old_obj = Order.objects.get(pk=obj.pk)
                print(f"DEBUG: old_status={old_obj.status}, new_status={obj.status}")
                if old_obj.status != obj.status:
                    print(f"DEBUG: Status changed! Sending email for {obj.status}")
                    if obj.status == 'confirmed':
                        self.send_confirmation_email(obj, request)
                    elif obj.status == 'shipped':
                        self.send_shipped_email(obj, request)
                else:
                    print("DEBUG: Status unchanged")
            except Exception as e:
                print(f"DEBUG ERROR: {e}")
        else:
            print("DEBUG: New order, skipping email")
        
        super().save_model(request, obj, form, change)

    def send_confirmation_email(self, order, request=None):
        try:
            send_order_email(
                order=order,
                subject='Your order has been confirmed!',
                template='emails/order_confirmation.html'
            )
            if request:
                self.message_user(request, f"Confirmation email sent to {order.email}", messages.SUCCESS)
        except Exception as e:
            if request:
                self.message_user(request, f"Failed: {e}", messages.ERROR)

    def send_shipped_email(self, order, request=None):
        try:
            send_order_email(
                order=order,
                subject='Your order has been shipped!',
                template='emails/shipped_email.html'
            )
            if request:
                self.message_user(request, f"Shipping email sent to {order.email}", messages.SUCCESS)
        except Exception as e:
            if request:
                self.message_user(request, f"Failed: {e}", messages.ERROR)

    send_confirmation_email.short_description = "Send confirmation email"
    send_shipped_email.short_description = "Send shipping email"