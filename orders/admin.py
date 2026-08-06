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
    actions = ['send_confirmation_email', 'send_shipped_email', 'send_processing_email', 'send_paid_email', 'send_delivered_email']

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
            'paid': '#2ecc71',
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
        if change:
            old_obj = Order.objects.get(pk=obj.pk)
            if old_obj.status != obj.status:
                status_email_map = {
                    'pending': self.send_pending_email,
                    'processing': self.send_processing_email,
                    'confirmed': self.send_confirmation_email,
                    'paid': self.send_paid_email,
                    'shipped': self.send_shipped_email,
                    'delivered': self.send_delivered_email,
                }
                send_email = status_email_map.get(obj.status)
                if send_email:
                    send_email(obj, request)
        super().save_model(request, obj, form, change)

    def send_pending_email(self, order, request=None):
        try:
            send_order_email(order=order, subject='Order received!', template='emails/custom_order_received.html')
            if request: self.message_user(request, f"Pending email sent to {order.email}", messages.SUCCESS)
        except Exception as e:
            if request: self.message_user(request, f"Failed: {e}", messages.ERROR)
    send_pending_email.short_description = "Send pending email"

    def send_processing_email(self, order, request=None):
        try:
            send_order_email(order=order, subject='Order is being processed', template='emails/processing_email.html')
            if request: self.message_user(request, f"Processing email sent to {order.email}", messages.SUCCESS)
        except Exception as e:
            if request: self.message_user(request, f"Failed: {e}", messages.ERROR)
    send_processing_email.short_description = "Send processing email"

    def send_confirmation_email(self, order, request=None):
        try:
            send_order_email(order=order, subject='Your order has been confirmed!', template='emails/order_confirmation.html')
            if request: self.message_user(request, f"Confirmation email sent to {order.email}", messages.SUCCESS)
        except Exception as e:
            if request: self.message_user(request, f"Failed: {e}", messages.ERROR)
    send_confirmation_email.short_description = "Send confirmation email"

    def send_paid_email(self, order, request=None):
        try:
            send_order_email(order=order, subject='Payment received!', template='emails/paid_email.html')
            if request: self.message_user(request, f"Paid email sent to {order.email}", messages.SUCCESS)
        except Exception as e:
            if request: self.message_user(request, f"Failed: {e}", messages.ERROR)
    send_paid_email.short_description = "Send paid email"

    def send_shipped_email(self, order, request=None):
        try:
            send_order_email(order=order, subject='Your order has been shipped!', template='emails/shipped_email.html')
            if request: self.message_user(request, f"Shipping email sent to {order.email}", messages.SUCCESS)
        except Exception as e:
            if request: self.message_user(request, f"Failed: {e}", messages.ERROR)
    send_shipped_email.short_description = "Send shipping email"

    def send_delivered_email(self, order, request=None):
        try:
            send_order_email(order=order, subject='Order delivered!', template='emails/delivered_email.html')
            if request: self.message_user(request, f"Delivered email sent to {order.email}", messages.SUCCESS)
        except Exception as e:
            if request: self.message_user(request, f"Failed: {e}", messages.ERROR)
    send_delivered_email.short_description = "Send delivered email"