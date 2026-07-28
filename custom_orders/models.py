from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class CustomOrder(models.Model):


    # ===============================
    # STATUS
    # ===============================


    STATUS_CHOICES = [

        ("new", _("New")),

        ("review", _("Under Review")),

        ("quote_sent", _("Quote Sent")),

        ("accepted", _("Accepted")),

        ("printing", _("Production")),

        ("finished", _("Finished")),

        ("shipped", _("Shipped")),

        ("cancelled", _("Cancelled")),

    ]



    # ===============================
    # SERVICE TYPE
    # ===============================


    SERVICE_CHOICES = [

        ("printing", _("3D Printing")),

        ("engraving", _("Engraving")),

        ("both", _("3D Printing + Engraving")),

    ]



    # ===============================
    # ENGRAVING TYPE
    # ===============================


    ENGRAVING_CHOICES = [

        ("none", _("No engraving")),

        ("text", _("Text engraving")),

        ("logo", _("Logo engraving")),

        ("image", _("Image engraving")),

    ]



    # ===============================
    # MATERIAL
    # ===============================


    MATERIAL_CHOICES = [

        ("PLA", "PLA"),

        ("PETG", "PETG"),

        ("ABS", "ABS"),

        ("TPU", "TPU"),

       

    ]





    # ===============================
    # CUSTOMER
    # ===============================


    user = models.ForeignKey(

        User,

        on_delete=models.SET_NULL,

        null=True,

        blank=True

    )



    name = models.CharField(

        max_length=100

    )



    email = models.EmailField()



    phone = models.CharField(

        max_length=50,

        blank=True

    )





    # ===============================
    # PROJECT
    # ===============================


    service = models.CharField(

        max_length=20,

        choices=SERVICE_CHOICES,

        default="printing"

    )



    description = models.TextField()





    # ===============================
    # ENGRAVING
    # ===============================


    engraving = models.BooleanField(

        default=False

    )



    engraving_type = models.CharField(

        max_length=20,

        choices=ENGRAVING_CHOICES,

        default="none"

    )



    engraving_text = models.CharField(

        max_length=255,

        blank=True

    )



    engraving_image = models.ImageField(

        upload_to="custom_orders/engraving/",

        blank=True,

        null=True

    )





    # ===============================
    # PRINT SETTINGS
    # ===============================


    material = models.CharField(

        max_length=20,

        choices=MATERIAL_CHOICES,

        default="PLA"

    )



    color = models.CharField(

        max_length=50,

        blank=True

    )




    width = models.DecimalField(

        max_digits=8,

        decimal_places=2,

        null=True,

        blank=True

    )



    height = models.DecimalField(

        max_digits=8,

        decimal_places=2,

        null=True,

        blank=True

    )



    depth = models.DecimalField(

        max_digits=8,

        decimal_places=2,

        null=True,

        blank=True

    )



    quantity = models.PositiveIntegerField(

        default=1

    )





    # ===============================
    # FILES
    # ===============================


    model_file = models.FileField(

        upload_to="custom_orders/files/",

        blank=True,

        null=True

    )



    image = models.ImageField(

        upload_to="custom_orders/images/",

        blank=True,

        null=True

    )





    # ===============================
    # ADMIN / PRICE
    # ===============================


    status = models.CharField(

        max_length=20,

        choices=STATUS_CHOICES,

        default="new"

    )



    estimated_price = models.DecimalField(

        max_digits=10,

        decimal_places=2,

        null=True,

        blank=True

    )



    admin_note = models.TextField(

        blank=True

    )





    # ===============================
    # DATES
    # ===============================


    created = models.DateTimeField(

        auto_now_add=True

    )



    updated = models.DateTimeField(

        auto_now=True

    )





    def __str__(self):

        return f"Custom Order #{self.id} - {self.name}"