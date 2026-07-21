from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from django.http import HttpResponse
from django.conf import settings
from io import BytesIO
import os

# Farby Velvet Creature
GOLD = HexColor('#d4af37')
BLACK = HexColor('#0a0a0a')
WHITE = HexColor('#ffffff')
GREY = HexColor('#8a8a7a')

# Cesty
BASE_DIR = settings.BASE_DIR
LOGO_PATH = os.path.join(BASE_DIR, 'static', 'images', 'logo.png')
FONTS_DIR = os.path.join(BASE_DIR, 'static', 'fonts')

# Registrácia EB Garamond fontov
pdfmetrics.registerFont(TTFont('EBGaramond', os.path.join(FONTS_DIR, 'EBGaramond-Regular.ttf')))
pdfmetrics.registerFont(TTFont('EBGaramond-Bold', os.path.join(FONTS_DIR, 'EBGaramond-Bold.ttf')))
pdfmetrics.registerFont(TTFont('EBGaramond-Italic', os.path.join(FONTS_DIR, 'EBGaramond-Italic.ttf')))
pdfmetrics.registerFont(TTFont('EBGaramond-SemiBold', os.path.join(FONTS_DIR, 'EBGaramond-SemiBold.ttf')))
pdfmetrics.registerFont(TTFont('EBGaramond-Medium', os.path.join(FONTS_DIR, 'EBGaramond-Medium.ttf')))


def generate_invoice(order):

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="facture_{order.order_number}.pdf"'

    pdf = canvas.Canvas(response, pagesize=A4)
    width, height = A4

    # =========================
    # POZADIE
    # =========================
    pdf.setFillColor(BLACK)
    pdf.rect(0, 0, width, height, fill=1)

    # =========================
    # ZLATÝ PRUH HORE
    # =========================
    pdf.setFillColor(GOLD)
    pdf.rect(0, height - 4, width, 4, fill=1)

    # =========================
    # LOGO
    # =========================
    if os.path.exists(LOGO_PATH):
        try:
            logo = ImageReader(LOGO_PATH)
            pdf.drawImage(logo, 40, height - 95, width=70, height=70, preserveAspectRatio=True)
            text_x = 125
        except:
            text_x = 40
    else:
        text_x = 40

    # =========================
    # HEADER
    # =========================
    pdf.setFillColor(GOLD)
    pdf.setFont("EBGaramond-SemiBold", 30)
    pdf.drawString(text_x, height - 58, "VELVET CREATURE")

    pdf.setFillColor(GREY)
    pdf.setFont("EBGaramond-Italic", 12)
    pdf.drawString(text_x, height - 78, "by Lubma3D")

    pdf.setFillColor(GOLD)
    pdf.setFont("EBGaramond-Bold", 18)
    pdf.drawRightString(width - 40, height - 55, "FACTURE")

    # =========================
    # ODDELOVAČ
    # =========================
    pdf.setStrokeColor(GOLD)
    pdf.setLineWidth(0.5)
    pdf.line(40, height - 105, width - 40, height - 105)

    # =========================
    # INFORMATIONS DE COMMANDE
    # =========================
    y = height - 135

    pdf.setFillColor(WHITE)
    pdf.setFont("EBGaramond-SemiBold", 15)
    pdf.drawString(40, y, "Informations de commande")

    y -= 26

    pdf.setFillColor(GREY)
    pdf.setFont("EBGaramond", 12)
    
    info_lines = [
        ("Numéro de commande :", f"{order.order_number}"),
        ("Date :", f"{order.created.strftime('%d.%m.%Y')}"),
        ("Statut :", f"{order.status.upper()}"),
        ("Paiement :", f"{order.payment_method}"),
    ]
    
    for label, value in info_lines:
        pdf.drawString(40, y, label)
        pdf.setFillColor(WHITE)
        pdf.drawString(210, y, value)
        pdf.setFillColor(GREY)
        y -= 20

    # =========================
    # CLIENT
    # =========================
    y -= 20

    pdf.setFillColor(WHITE)
    pdf.setFont("EBGaramond-SemiBold", 15)
    pdf.drawString(40, y, "Client")

    y -= 26

    pdf.setFillColor(GREY)
    pdf.setFont("EBGaramond", 12)
    
    customer_lines = [
        f"{order.first_name} {order.last_name}",
        order.address or "",
        f"{order.city or ''} {order.country or ''}",
        order.email or "",
    ]

    for line in customer_lines:
        if line.strip():
            pdf.drawString(40, y, line)
            y -= 20

    # =========================
    # LIVRAISON
    # =========================
    if order.shipping_method:
        y -= 22
        pdf.setFillColor(WHITE)
        pdf.setFont("EBGaramond-SemiBold", 15)
        pdf.drawString(40, y, "Livraison")
        y -= 24
        pdf.setFillColor(GREY)
        pdf.setFont("EBGaramond", 12)
        pdf.drawString(40, y, f"{order.shipping_method.name} - EUR {order.shipping_price}")

    # =========================
    # ODDELOVAČ
    # =========================
    y -= 30
    pdf.setStrokeColor(GOLD)
    pdf.setLineWidth(0.3)
    pdf.line(40, y, width - 40, y)
    y -= 28

    # =========================
    # PRODUITS
    # =========================
    pdf.setFillColor(WHITE)
    pdf.setFont("EBGaramond-SemiBold", 15)
    pdf.drawString(40, y, "Produits")
    y -= 28

    # Hlavička tabuľky
    pdf.setFillColor(GOLD)
    pdf.setFont("EBGaramond-Bold", 11)
    pdf.drawString(40, y, "Produit")
    pdf.drawRightString(width - 180, y, "Qté")
    pdf.drawRightString(width - 120, y, "Prix")
    pdf.drawRightString(width - 40, y, "Total")
    y -= 6

    pdf.setStrokeColor(GOLD)
    pdf.setLineWidth(0.3)
    pdf.line(40, y, width - 40, y)
    y -= 20

    # Položky
    pdf.setFillColor(GREY)
    pdf.setFont("EBGaramond", 11)

    for item in order.items.all():
        pdf.drawString(40, y, item.product.name[:35])
        pdf.drawRightString(width - 180, y, str(item.quantity))
        pdf.drawRightString(width - 120, y, f"EUR {item.price}")
        pdf.setFillColor(GOLD)
        pdf.drawRightString(width - 40, y, f"EUR {item.get_total()}")
        pdf.setFillColor(GREY)
        y -= 20
        
        pdf.setStrokeColor(HexColor('#2a1a1a'))
        pdf.setLineWidth(0.1)
        pdf.line(40, y + 8, width - 40, y + 8)

    # =========================
    # TOTAL
    # =========================
    y -= 22

    pdf.setStrokeColor(GOLD)
    pdf.setLineWidth(0.5)
    pdf.line(40, y + 10, width - 40, y + 10)

    y -= 5

    pdf.setFillColor(GOLD)
    pdf.setFont("EBGaramond-Bold", 22)
    pdf.drawRightString(width - 40, y, f"TOTAL : EUR {order.total_price}")

    # =========================
    # FOOTER
    # =========================
    pdf.setStrokeColor(GOLD)
    pdf.setLineWidth(0.3)
    pdf.line(40, 80, width - 40, 80)

    pdf.setFillColor(GREY)
    pdf.setFont("EBGaramond-Italic", 11)
    pdf.drawString(40, 58, "Merci de soutenir Velvet Creature.")
    
    pdf.setFillColor(GOLD)
    pdf.setFont("EBGaramond-SemiBold", 12)
    pdf.drawString(40, 40, "Velvet Creature by Lubma3D")
    
    pdf.setFillColor(GREY)
    pdf.setFont("EBGaramond", 9)
    pdf.drawRightString(width - 40, 40, "www.velvetcreature.fr")

    pdf.save()
    return response



def generate_invoice_bytes(order):

    buffer = BytesIO()

    pdf = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    # POZADIE
    pdf.setFillColor(BLACK)
    pdf.rect(0, 0, width, height, fill=1)

    # ZLATÝ PRUH
    pdf.setFillColor(GOLD)
    pdf.rect(0, height - 4, width, 4, fill=1)

    # LOGO
    if os.path.exists(LOGO_PATH):
        try:
            logo = ImageReader(LOGO_PATH)
            pdf.drawImage(logo, 40, height - 95, width=70, height=70, preserveAspectRatio=True)
            text_x = 125
        except:
            text_x = 40
    else:
        text_x = 40

    # HEADER
    pdf.setFillColor(GOLD)
    pdf.setFont("EBGaramond-SemiBold", 30)
    pdf.drawString(text_x, height - 58, "VELVET CREATURE")

    pdf.setFillColor(GREY)
    pdf.setFont("EBGaramond-Italic", 12)
    pdf.drawString(text_x, height - 78, "by Lubma3D")

    # INFO
    y = height - 140
    pdf.setFillColor(WHITE)
    pdf.setFont("EBGaramond", 13)
    pdf.drawString(40, y, f"Order: {order.order_number}")
    y -= 24
    pdf.drawString(40, y, f"Customer: {order.first_name} {order.last_name}")
    y -= 24
    pdf.setFillColor(GOLD)
    pdf.setFont("EBGaramond-Bold", 16)
    pdf.drawString(40, y, f"Total: EUR {order.total_price}")

    y -= 32
    pdf.setFillColor(WHITE)
    pdf.setFont("EBGaramond-SemiBold", 12)
    pdf.drawString(40, y, "Products:")
    y -= 22
    pdf.setFillColor(GREY)
    pdf.setFont("EBGaramond", 11)
    for item in order.items.all():
        pdf.drawString(40, y, f"{item.product.name} x{item.quantity}")
        y -= 20

    pdf.save()
    buffer.seek(0)
    return buffer.read()