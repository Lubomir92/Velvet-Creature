from django.contrib import admin, messages
from .models import Order, OrderItem
from .email import send_order_email


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['price']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['first_name', 'last_name', 'email', 'id']
    inlines = [OrderItemInline]
    actions = ['send_confirmation_email', 'send_shipped_email']

    def save_model(self, request, obj, form, change):
        """
        Pri uložení objednávky v admine skontroluje, či sa zmenil stav,
        a ak áno, pošle príslušný e-mail.
        """
        if change:  # Ak sa upravuje existujúca objednávka
            old_obj = Order.objects.get(pk=obj.pk)
            if old_obj.status != obj.status:
                # Stav sa zmenil - odošleme e-mail podľa nového stavu
                if obj.status == 'confirmed':
                    self.send_confirmation_email(obj, request)
                elif obj.status == 'shipped':
                    self.send_shipped_email(obj, request)
        
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
                self.message_user(request, f"Failed to send confirmation email: {e}", messages.ERROR)

    def send_shipped_email(self, order, request=None):
        try:
            send_order_email(
                order=order,
                subject='Your order has been shipped!',
                template='emails/order_shipped.html'
            )
            if request:
                self.message_user(request, f"Shipping email sent to {order.email}", messages.SUCCESS)
        except Exception as e:
            if request:
                self.message_user(request, f"Failed to send shipping email: {e}", messages.ERROR)

    send_confirmation_email.short_description = "Send confirmation email"
    send_shipped_email.short_description = "Send shipping email"