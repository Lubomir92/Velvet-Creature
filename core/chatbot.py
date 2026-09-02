from django.utils.translation import gettext as _

# Odpovede pre bota v troch jazykoch
BOT_RESPONSES = {
    "fr": {
        "greeting": "Bonjour! Je suis l'assistant Velvet Creature. Comment puis-je vous aider?",
        "shipping": "Nous livrons en France (2-5 jours), en Europe (5-10 jours) et à l'international (10-20 jours). Les commandes sont expédiées après 3-7 jours ouvrés de fabrication.",
        "payment": "Nous acceptons les paiements par carte bancaire (Stripe) et par virement bancaire.",
        "products": "Nos produits sont imprimés en 3D en PLA biodégradable et finis à la main. Chaque pièce est unique!",
        "return": "Vous disposez de 14 jours pour changer d'avis (droit de rétractation). Les produits personnalisés ne sont pas repris.",
        "contact": "Pour toute question, contactez-nous à lubma3D@outlook.fr",
        "default": "Je suis désolé, je ne comprends pas. Essayez de demander sur: livraison, paiement, produits, retour ou contact.",
    },
    "en": {
        "greeting": "Hello! I'm the Velvet Creature assistant. How can I help you?",
        "shipping": "We deliver to France (2-5 days), Europe (5-10 days) and internationally (10-20 days). Orders ship after 3-7 working days of production.",
        "payment": "We accept credit card (Stripe) and bank transfer payments.",
        "products": "Our products are 3D printed in biodegradable PLA and hand-finished. Each piece is unique!",
        "return": "You have 14 days to change your mind (withdrawal right). Custom products cannot be returned.",
        "contact": "For any questions, contact us at lubma3D@outlook.fr",
        "default": "I'm sorry, I don't understand. Try asking about: shipping, payment, products, returns or contact.",
    },
    "sk": {
        "greeting": "Ahoj! Som asistent Velvet Creature. Ako vám môžem pomôcť?",
        "shipping": "Doručujeme do Francúzska (2-5 dní), Európy (5-10 dní) a medzinárodne (10-20 dní). Objednávky odosielame po 3-7 pracovných dňoch výroby.",
        "payment": "Prijímame platby kartou (Stripe) a bankovým prevodom.",
        "products": "Naše produkty sú 3D tlačené z biologicky rozložiteľného PLA a ručne dokončené. Každý kus je jedinečný!",
        "return": "Máte 14 dní na rozmyslenie (právo na odstúpenie). Zákazkové produkty nie je možné vrátiť.",
        "contact": "Pre akékoľvek otázky nás kontaktujte na lubma3D@outlook.fr",
        "default": "Prepáčte, nerozumiem. Skúste sa opýtať na: dopravu, platbu, produkty, vrátenie alebo kontakt.",
    }
}

# Kľúčové slová pre rozpoznanie otázky
KEYWORDS = {
    "shipping": ["doprava", "livraison", "delivery", "shipping", "doručenie", "expédition", "dodanie"],
    "payment": ["platba", "paiement", "payment", "card", "karta", "carte", "virement", "prevod", "stripe", "bank"],
    "products": ["produkt", "produit", "product", "matériau", "material", "materiál", "pla", "3d", "impression", "tlač"],
    "return": ["retour", "vrátenie", "return", "rembours", "vrátiť", "14 jours", "14 dní", "odstúpenie", "rétractation"],
    "contact": ["contact", "email", "kontakt", "kde", "ou", "where", "nájsť", "trouver"],
}


def get_bot_response(message, language="fr"):
    """
    Vráti odpoveď bota na základe správy a jazyka.
    """
    message_lower = message.lower()
    responses = BOT_RESPONSES.get(language, BOT_RESPONSES["fr"])
    
    # Hľadáme kľúčové slová v správe
    for category, words in KEYWORDS.items():
        for word in words:
            if word.lower() in message_lower:
                return responses.get(category, responses["default"])
    
    # Ak žiadne kľúčové slovo nenájdené, vráť default
    return responses["default"]