from django.db import models
from django.contrib.auth.models import User
from products.models import Product
import uuid



class Order(models.Model):


    STATUS_CHOICES = [

        ("pending", "Pending"),
        ("paid", "Paid"),
        ("shipped", "Shipped"),
        ("delivered", "Delivered"),

    ]



    order_number = models.CharField(
        max_length=20,
        blank=True,
        null=True
)



    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders"
    )



    email = models.EmailField(
        blank=True,
        null=True
    )


    first_name = models.CharField(
        max_length=100,
        blank=True
    )


    last_name = models.CharField(
        max_length=100,
        blank=True
    )


    address = models.CharField(
        max_length=255,
        blank=True
    )


    city = models.CharField(
        max_length=100,
        blank=True
    )


    country = models.CharField(
        max_length=100,
        blank=True
    )



    note = models.TextField(
        blank=True
    )



    payment_method = models.CharField(
        max_length=50,
        default="Stripe"
    )



    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )



    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )



    created = models.DateTimeField(
        auto_now_add=True
    )


    updated = models.DateTimeField(
        auto_now=True
    )



    def save(self, *args, **kwargs):

        if not self.order_number:

            self.order_number = (
                "VC-" +
                uuid.uuid4().hex[:8].upper()
            )

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



    quantity = models.PositiveIntegerField(
        default=1
    )



    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )



    def get_total(self):

        return self.quantity * self.price