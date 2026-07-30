import os
import resend
from django.template.loader import render_to_string


def send_order_email(order, subject, template):
    try:
        html = render_to_string(template, {"order": order})
        
        resend.api_key = os.getenv("RESEND_API_KEY")
        resend.Emails.send({
            "from": "Velvet Creature <onboarding@resend.dev>",
            "to": [order.email],
            "subject": subject,
            "html": html,
        })
    except Exception as e:
        print(f"Email error: {e}")