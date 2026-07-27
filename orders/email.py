import os
import resend


def send_order_email(order, subject, template):
    try:
        resend.api_key = os.getenv("RESEND_API_KEY")
        resend.Emails.send({
            "from": "Velvet Creature <onboarding@resend.dev>",
            "to": [order.email],
            "subject": subject,
            "text": f"Order: {order.order_number}\nStatus: {order.status}\nTotal: €{order.total_price}",
        })
    except Exception as e:
        print(f"Email error: {e}")