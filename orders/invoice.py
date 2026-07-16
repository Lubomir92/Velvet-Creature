from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm

from django.http import HttpResponse



def generate_invoice(order):


    response = HttpResponse(
        content_type="application/pdf"
    )


    response["Content-Disposition"] = (
        f'attachment; filename="invoice_{order.order_number}.pdf"'
    )



    pdf = canvas.Canvas(
        response,
        pagesize=A4
    )



    width, height = A4



    # =========================
    # HEADER
    # =========================


    pdf.setFont(
        "Helvetica-Bold",
        24
    )


    pdf.drawString(
        40,
        height - 60,
        "VELVET CREATURE"
    )



    pdf.setFont(
        "Helvetica",
        11
    )


    pdf.drawString(
        40,
        height - 85,
        "by Lubma3D"
    )



    pdf.setFont(
        "Helvetica-Bold",
        16
    )


    pdf.drawRightString(
        width - 40,
        height - 60,
        "INVOICE"
    )



    # =========================
    # ORDER INFO
    # =========================


    y = height - 130



    pdf.setFont(
        "Helvetica",
        11
    )



    pdf.drawString(
        40,
        y,
        f"Order number: {order.order_number}"
    )


    y -= 20


    pdf.drawString(
        40,
        y,
        f"Date: {order.created.strftime('%d.%m.%Y')}"
    )


    y -= 20


    pdf.drawString(
        40,
        y,
        f"Status: {order.status.upper()}"
    )





    # =========================
    # CUSTOMER
    # =========================


    y -= 50


    pdf.setFont(
        "Helvetica-Bold",
        12
    )


    pdf.drawString(
        40,
        y,
        "Customer:"
    )



    pdf.setFont(
        "Helvetica",
        11
    )


    y -= 20


    customer_lines = [

        f"{order.first_name} {order.last_name}",

        order.address,

        order.city,

        order.country,

        order.email,

    ]



    for line in customer_lines:


        pdf.drawString(
            40,
            y,
            line or ""
        )


        y -= 18





    # =========================
    # PRODUCTS
    # =========================


    y -= 30



    pdf.setFont(
        "Helvetica-Bold",
        12
    )


    pdf.drawString(
        40,
        y,
        "Products:"
    )



    y -= 25



    pdf.setFont(
        "Helvetica",
        11
    )



    for item in order.items.all():

        text = (
            f"{item.product.name}   "
            f"x{item.quantity}     "
            f"EUR {item.price}"
        )


        pdf.drawString(
            40,
            y,
            text
        )


        y -= 20






    # =========================
    # TOTAL
    # =========================


    y -= 20



    pdf.setFont(
        "Helvetica-Bold",
        15
    )


    pdf.drawString(
        40,
        y,
        f"TOTAL: EUR {order.total_price}"
    )



    # =========================
    # FOOTER
    # =========================


    pdf.setFont(
        "Helvetica",
        10
    )


    pdf.drawString(
        40,
        50,
        "Thank you for supporting Velvet Creature."
    )


    pdf.drawString(
        40,
        35,
        "Velvet Creature by Lubma3D"
    )



    pdf.save()


    return response
def generate_invoice_bytes(order):

    from io import BytesIO


    buffer = BytesIO()


    pdf = canvas.Canvas(
        buffer,
        pagesize=A4
    )


    width, height = A4


    pdf.setFont(
        "Helvetica-Bold",
        24
    )

    pdf.drawString(
        40,
        height - 60,
        "VELVET CREATURE"
    )


    pdf.setFont(
        "Helvetica",
        11
    )

    pdf.drawString(
        40,
        height - 85,
        "by Lubma3D"
    )


    pdf.setFont(
        "Helvetica",
        12
    )


    pdf.drawString(
        40,
        height - 130,
        f"Order: {order.order_number}"
    )


    pdf.drawString(
        40,
        height - 150,
        f"Customer: {order.first_name} {order.last_name}"
    )


    pdf.drawString(
        40,
        height - 170,
        f"Total: EUR {order.total_price}"
    )


    y = height - 220


    pdf.drawString(
        40,
        y,
        "Products:"
    )


    y -= 20


    for item in order.items.all():

        pdf.drawString(
            40,
            y,
            f"{item.product.name} x{item.quantity}"
        )

        y -= 20



    pdf.save()


    buffer.seek(0)


    return buffer.read()