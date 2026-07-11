from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings



# ==================================================
# EMAIL TO CUSTOMER
# ==================================================

def send_custom_order_received_email(order):


    subject = "Custom Order Received - Velvet Creature"



    text_message = f"""
Hello {order.name},


Thank you for your custom project request.


We have received your order and our team will review it shortly.


Order number:
#{order.id}


Service:
{order.get_service_display()}


Material:
{order.material}


Description:
{order.description}


Engraving:
{"Yes" if order.engraving else "No"}



Velvet Creature
"""



    html_message = render_to_string(

        "emails/custom_order_received.html",

        {
            "order": order
        }

    )



    email = EmailMultiAlternatives(

        subject,

        text_message,

        settings.DEFAULT_FROM_EMAIL,

        [
            order.email
        ]

    )



    email.attach_alternative(

        html_message,

        "text/html"

    )



    email.send()





# ==================================================
# EMAIL TO ADMIN
# ==================================================

def send_admin_new_custom_order_email(order):


    subject = (
        f"NEW CUSTOM ORDER #{order.id} - Velvet Creature"
    )



    message = f"""
New custom project received!


Customer:

{order.name}


Email:

{order.email}


Phone:

{order.phone}



Service:

{order.get_service_display()}



Material:

{order.material}



Quantity:

{order.quantity}



Description:

{order.description}



Engraving:

{"Yes" if order.engraving else "No"}



Engraving type:

{order.get_engraving_type_display()}



Velvet Creature Admin
"""



    email = EmailMultiAlternatives(

        subject,

        message,

        settings.DEFAULT_FROM_EMAIL,

        [
            settings.DEFAULT_ADMIN_EMAIL
        ]

    )


    email.send()