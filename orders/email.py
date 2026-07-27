import os
import resend


def send_order_email(order, subject, template):

    # Jednoduchá textová správa
    body = f"""Order: {order.order_number}
Status: {order.status}
Total: €{order.total_price}
Customer: {order.first_name} {order.last_name}
Email: {order.email}
"""

    try:
        resend.api_key = os.getenv("RESEND_API_KEY")
        resend.Emails.send({
            "from": "Velvet Creature <onboarding@resend.dev>",
            "to": [order.email],
            "subject": subject,
            "text": body,
        })
    except Exception as e:
        print(f"Email error: {e}")