from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_order_email(order, subject, template):

    html = render_to_string(
        template,
        {
            "order": order
        }
    )

    email = EmailMultiAlternatives(
        subject=subject,
        body="",
        to=[order.email]
    )

    email.attach_alternative(
        html,
        "text/html"
    )

    email.send()