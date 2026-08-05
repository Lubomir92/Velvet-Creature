import os
import resend


# ==================================================
# EMAIL TO CUSTOMER
# ==================================================

def send_custom_order_received_email(order):

    try:
        resend.api_key = os.getenv("RESEND_API_KEY")
        resend.Emails.send({
            "from": "Velvet Creature <onboarding@resend.dev>",
            "to": [order.email],
            "subject": f"Custom Order Received - Velvet Creature",
            "html": f"""
            <h2>Hello {order.name},</h2>
            <p>Thank you for your custom project request.</p>
            <p>We have received your order and our team will review it shortly.</p>
            <hr>
            <p><strong>Order number:</strong> #{order.id}</p>
            <p><strong>Service:</strong> {order.get_service_display()}</p>
            <p><strong>Material:</strong> {order.material}</p>
            <p><strong>Description:</strong> {order.description}</p>
            <p><strong>Engraving:</strong> {"Yes" if order.engraving else "No"}</p>
            <br>
            <p>Velvet Creature</p>
            """,
        })
    except Exception as e:
        print(f"Email error: {e}")


# ==================================================
# EMAIL TO ADMIN
# ==================================================

def send_admin_new_custom_order_email(order):

    try:
        resend.api_key = os.getenv("RESEND_API_KEY")
        resend.Emails.send({
            "from": "Velvet Creature <onboarding@resend.dev>",
            "to": ["lubma3D@outlook.fr"],
            "subject": f"🔔 NEW CUSTOM ORDER #{order.id} - Velvet Creature",
            "html": f"""
            <h2>New custom project received!</h2>
            <hr>
            <p><strong>Customer:</strong> {order.name}</p>
            <p><strong>Email:</strong> {order.email}</p>
            <p><strong>Phone:</strong> {order.phone}</p>
            <p><strong>Service:</strong> {order.get_service_display()}</p>
            <p><strong>Material:</strong> {order.material}</p>
            <p><strong>Quantity:</strong> {order.quantity}</p>
            <p><strong>Description:</strong> {order.description}</p>
            <p><strong>Engraving:</strong> {"Yes" if order.engraving else "No"}</p>
            <p><strong>Engraving type:</strong> {order.get_engraving_type_display()}</p>
            <br>
            <p><a href="https://www.velvetcreature.fr/admin/">View in Admin</a></p>
            """,
        })
    except Exception as e:
        print(f"Email error: {e}")