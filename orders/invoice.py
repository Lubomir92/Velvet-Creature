from reportlab.pdfgen import canvas
from django.http import HttpResponse



def generate_invoice(order):

    response = HttpResponse(
        content_type="application/pdf"
    )


    response["Content-Disposition"] = (
        f'attachment; filename="invoice_{order.order_number}.pdf"'
    )



    pdf = canvas.Canvas(response)



    pdf.setFont(
        "Helvetica-Bold",
        18
    )


    pdf.drawString(
        50,
        800,
        "VELVET CREATURE"
    )



    pdf.setFont(
        "Helvetica",
        12
    )


    pdf.drawString(
        50,
        770,
        "Invoice"
    )



    pdf.drawString(
        50,
        740,
        f"Order number: {order.order_number}"
    )



    pdf.drawString(
        50,
        710,
        f"Customer: {order.first_name} {order.last_name}"
    )



    pdf.drawString(
        50,
        690,
        f"Address: {order.address}"
    )



    pdf.drawString(
        50,
        670,
        f"Date: {order.created.strftime('%d.%m.%Y')}"
    )



    y = 630



    pdf.drawString(
        50,
        y,
        "Products:"
    )


    y -= 30



    for item in order.items.all():

        pdf.drawString(
            50,
            y,
            f"{item.product.name} x {item.quantity} - EUR {item.price}"
        )

        y -= 25



    y -= 20


    pdf.setFont(
        "Helvetica-Bold",
        14
    )



    pdf.drawString(
        50,
        y,
        f"TOTAL: EUR {order.total_price}"
    )



    y -= 40



    pdf.setFont(
        "Helvetica",
        10
    )



    pdf.drawString(
        50,
        y,
        "Thank you for shopping with Velvet Creature"
    )



    pdf.save()


    return response