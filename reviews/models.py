from django.db import models
from django.contrib.auth.models import User
from products.models import Product



class Review(models.Model):


    RATING_CHOICES = [

        (1, "★"),
        (2, "★★"),
        (3, "★★★"),
        (4, "★★★★"),
        (5, "★★★★★"),

    ]


    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="reviews"
    )


    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )


    rating = models.IntegerField(
        choices=RATING_CHOICES
    )


    comment = models.TextField(
        max_length=500
    )


    created = models.DateTimeField(
        auto_now_add=True
    )



    def __str__(self):

        return f"{self.product.name} - {self.rating}"
    class Meta:
        unique_together = ("product", "user")