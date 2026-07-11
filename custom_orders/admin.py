from django.contrib import admin

from .models import CustomOrder



@admin.register(CustomOrder)
class CustomOrderAdmin(admin.ModelAdmin):


    # ===============================
    # LIST VIEW
    # ===============================


    list_display = (

        "id",

        "name",

        "service",

        "engraving",

        "material",

        "quantity",

        "status",

        "estimated_price",

        "created",

    )



    list_filter = (

        "status",

        "service",

        "engraving",

        "material",

        "created",

    )



    search_fields = (

        "name",

        "email",

        "description",

        "engraving_text",

    )



    readonly_fields = (

        "created",

        "updated",

    )





    # ===============================
    # FORM LAYOUT
    # ===============================


    fieldsets = (



        (

            "Customer",

            {

                "fields": (

                    "user",

                    "name",

                    "email",

                    "phone",

                )

            }

        ),




        (

            "Service",

            {

                "fields": (

                    "service",

                    "description",

                )

            }

        ),




        (

            "Engraving",

            {

                "fields": (

                    "engraving",

                    "engraving_type",

                    "engraving_text",

                    "engraving_image",

                )

            }

        ),




        (

            "3D Printing",

            {

                "fields": (

                    "material",

                    "color",

                    "width",

                    "height",

                    "depth",

                    "quantity",

                )

            }

        ),




        (

            "Uploaded files",

            {

                "fields": (

                    "model_file",

                    "image",

                )

            }

        ),




        (

            "Production",

            {

                "fields": (

                    "status",

                    "estimated_price",

                    "admin_note",

                )

            }

        ),




        (

            "Dates",

            {

                "fields": (

                    "created",

                    "updated",

                )

            }

        ),


    )