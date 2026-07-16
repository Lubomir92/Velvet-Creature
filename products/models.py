from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name



class Product(models.Model):
    # ==========================================
    # BASIC
    # ==========================================
    name = models.CharField(max_length=200)

    slug = models.SlugField(unique=True)

    description = models.TextField(blank=True)

    short_description = models.CharField(
        max_length=250,
        blank=True
    )


    # ==========================================
    # IMAGE
    # ==========================================
    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True
    )


    # ==========================================
    # PRODUCT INFO
    # ==========================================
    sku = models.CharField(
        max_length=50,
        blank=True
    )

    material = models.CharField(
        max_length=150,
        blank=True
    )

    size = models.CharField(
        max_length=100,
        blank=True
    )

    weight = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0
    )


    # ==========================================
    # PRICE
    # ==========================================
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    stock = models.PositiveIntegerField(
        default=0
    )

    featured = models.BooleanField(
        default=False
    )


    # ==========================================
    # CATEGORY
    # ==========================================
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )


    # ==========================================
    # DATES
    # ==========================================
    created = models.DateTimeField(
        auto_now_add=True
    )


    # ==========================================
    # STRING
    # ==========================================
    def __str__(self):
        return self.name





# ==================================================
# PRODUCT GALLERY IMAGES
# ==================================================

class ProductImage(models.Model):

    product = models.ForeignKey(
        Product,
        related_name="images",
        on_delete=models.CASCADE
    )


    image = models.ImageField(
        upload_to="products/gallery/"
    )


    alt_text = models.CharField(
        max_length=200,
        blank=True
    )


    created = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return f"{self.product.name} image"