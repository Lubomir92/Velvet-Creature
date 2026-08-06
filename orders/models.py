from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from products.models import Product
import uuid
from decimal import Decimal


class ShippingMethod(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=200, blank=True)
    website = models.URLField(blank=True)
    logo = models.CharField(max_length=10, blank=True, help_text="Emoji logo")
    is_active = models.BooleanField(default=True)
    sort_order = models.IntegerField(default=0)

    class Meta:
        ordering = ["sort_order"]
        verbose_name = "Shipping Method"
        verbose_name_plural = "Shipping Methods"

    def __str__(self):
        return f"{self.logo} {self.name} - €{self.price}"


class Order(models.Model):

    STATUS_CHOICES = [
        ("pending", _("Pending")),
        ("paid", _("Paid")),
        ("processing", _("Processing")),
        ("shipped", _("Shipped")),
        ("delivered", _("Delivered")),
    ]

    order_number = models.CharField(max_length=20, blank=True, null=True)

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders"
    )

    email = models.EmailField(blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=50, blank=True, default="")
    postal_code = models.CharField(max_length=20, blank=True, default="")
    relay_point = models.CharField(max_length=100, blank=True, default="")
    note = models.TextField(blank=True)

    payment_method = models.CharField(max_length=50, default="Stripe")
    
    # Doprava
    shipping_method = models.ForeignKey(
        "ShippingMethod",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    shipping_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    carrier = models.CharField(max_length=100, blank=True, null=True)
    tracking_number = models.CharField(max_length=200, blank=True, null=True)

    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    stock_updated = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = "VC-" + uuid.uuid4().hex[:8].upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderItem(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items"
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def get_total(self):
        return self.quantity * self.price