import os
import resend
import base64
from django.template.loader import render_to_string
from .invoice import generate_invoice_bytes


def send_order_email(order, subject, template):
    try:
        html = render_to_string(template, {"order": order})
        
        pdf_bytes = generate_invoice_bytes(order)
        pdf_base64 = base64.b64encode(pdf_bytes).decode('utf-8')
        
        resend.api_key = os.getenv("RESEND_API_KEY")
        resend.Emails.send({
            "from": "Velvet Creature <info@velvetcreature.fr>",
            "to": [order.email],
            "subject": subject,
            "html": html,
            "attachments": [
                {
                    "filename": f"facture_{order.order_number}.pdf",
                    "content": pdf_base64,
                    "content_type": "application/pdf",
                }
            ],
        })
    except Exception as e:
        print(f"Email error: {e}")