

# Odpovede pre bota v troch jazykoch
from django.utils.translation import gettext as _

# Odpovede pre bota v troch jazykoch
BOT_RESPONSES = {
    "fr": {
        "greeting": "Bonjour! Je suis Mr.Citrouille, l'assistant de Velvet Creature. Comment puis-je vous aider?",
        
        "shipping": "Nous livrons en France (2-5 jours), en Europe (5-10 jours) et à l'international (10-20 jours). Les commandes sont expédiées après 3-7 jours ouvrés de fabrication. Modes de livraison: Mondial Relay (point relais et domicile) et Shop to Shop by Chronopost.",
        
        "payment": "Nous acceptons les paiements par carte bancaire (Stripe) et par virement bancaire. Le paiement est 100% sécurisé et vos données bancaires ne sont jamais stockées sur nos serveurs.",
        
        "products": "Nos produits sont imprimés en 3D en PLA (acide polylactique), PETG ou TPU. Le PLA est biodégradable et non toxique, le PETG est résistant à l'eau et aux chocs, et le TPU est flexible et élastique. Chaque pièce est finie à la main et donc unique!",

"materials": "Nous utilisons trois matériaux: le PLA (écologique et biodégradable), le PETG (résistant à l'eau et aux chocs) et le TPU (flexible et élastique). Chaque matériau a ses avantages selon l'usage. Chaque pièce est finie à la main.",
        
        "sizes": "Les tailles varient selon les produits. Consultez la page de chaque produit pour les dimensions exactes. Si vous avez besoin d'une taille spécifique, n'hésitez pas à nous contacter!",
        
        "custom": "Nous proposons des commandes personnalisées! Vous pouvez demander un modèle sur mesure, une gravure de texte ou de logo. Allez sur la page 'Commande personnalisée' pour décrire votre projet.",
        
        "engraving": "Nous proposons la gravure de texte, de logo ou d'image sur la plupart de nos produits. Envoyez-nous votre idée sur la page 'Commande personnalisée' et nous vous enverrons un devis!",
        
        "return": "Vous disposez de 14 jours pour changer d'avis (droit de rétractation selon l'Article L221-18 du Code de la Consommation). Les produits personnalisés ne sont pas repris. Pour un retour, contactez-nous à lubma3D@outlook.fr",
        
        "refund": "Le remboursement est effectué sous 14 jours après réception et vérification des articles retournés. Le montant est remboursé via le même moyen de paiement que la transaction d'origine.",
        
        "tracking": "Dès que votre commande est expédiée, vous recevrez un email avec le numéro de suivi. Vous pouvez également consulter vos commandes dans votre compte.",
        
        "stock": "La plupart de nos produits sont imprimés sur commande. Si un produit est marqué 'En stock', il est disponible immédiatement. Sinon, comptez 3-7 jours ouvrés de fabrication.",
        
        "care": "Nos produits sont fragiles. Nettoyez-les délicatement avec un chiffon doux sec. Évitez l'exposition prolongée au soleil et à la chaleur. Ne les mettez pas dans l'eau.",
        
        "discounts": "Pour connaître nos promotions en cours, suivez-nous sur nos réseaux sociaux! Nous publions régulièrement des offres exclusives pour nos abonnés.",
        
        "social": "Retrouvez-nous sur Instagram et TikTok! Cherchez 'VelvetCreature' pour voir nos créations et nos coulisses.",
        
        "about": "Velvet Creature est une entreprise artisanale spécialisée dans la création de créatures gothiques imprimées en 3D. Chaque pièce est créée avec passion par Lubma3D en France.",
        
        "contact": "Pour toute question, contactez-nous à lubma3D@outlook.fr. Nous répondons généralement sous 24-48h.",
        
        "help": "Je peux vous aider sur: livraison, paiement, produits, matériaux, tailles, commandes personnalisées, gravure, retours, remboursements, suivi de commande, stock, entretien, promos, réseaux sociaux, à propos.",
        
        "default": "Je suis désolé, je ne comprends pas. Je peux vous aider sur: livraison, paiement, produits, retours, suivi, matériaux, tailles, commandes personnalisées, gravure, remboursements, stock, entretien, promos, réseaux sociaux ou contact.",
    },
    "en": {
        "greeting": "Hello! I'm Mr.Citrouille, the Velvet Creature assistant. How can I help you?",
        
        "shipping": "We deliver to France (2-5 days), Europe (5-10 days) and internationally (10-20 days). Orders ship after 3-7 working days of production. Delivery methods: Mondial Relay (pickup points and home delivery) and Shop to Shop by Chronopost.",
        
        "payment": "We accept credit card (Stripe) and bank transfer payments. Payment is 100% secure and your card details are never stored on our servers.",
        
        "products": "Our products are 3D printed in PLA (polylactic acid), PETG or TPU. PLA is biodegradable and non-toxic, PETG is water and impact resistant, and TPU is flexible and elastic. Each piece is hand-finished and therefore unique!",

"materials": "We use three materials: PLA (eco-friendly and biodegradable), PETG (water and impact resistant) and TPU (flexible and elastic). Each material has its advantages depending on use. Each piece is hand-finished.",
        
        "sizes": "Sizes vary by product. Check each product page for exact dimensions. If you need a specific size, don't hesitate to contact us!",
        
        "custom": "We offer custom orders! You can request a bespoke model, text engraving or logo engraving. Go to the 'Custom Order' page to describe your project.",
        
        "engraving": "We offer text, logo or image engraving on most of our products. Send us your idea on the 'Custom Order' page and we'll send you a quote!",
        
        "return": "You have 14 days to change your mind (withdrawal right according to Article L221-18 of the French Consumer Code). Custom products cannot be returned. For returns, contact us at lubma3D@outlook.fr",
        
        "refund": "Refunds are processed within 14 days after receiving and checking returned items. The amount is refunded via the same payment method as the original transaction.",
        
        "tracking": "As soon as your order is shipped, you'll receive an email with the tracking number. You can also check your orders in your account.",
        
        "stock": "Most of our products are printed to order. If a product is marked 'In Stock', it's available immediately. Otherwise, allow 3-7 working days for production.",
        
        "care": "Our products are fragile. Clean them gently with a dry soft cloth. Avoid prolonged exposure to sunlight and heat. Do not put them in water.",
        
        "discounts": "For current promotions, follow us on social media! We regularly post exclusive offers for our subscribers.",
        
        "social": "Find us on Instagram and TikTok! Search for 'VelvetCreature' to see our creations and behind-the-scenes.",
        
        "about": "Velvet Creature is an artisanal company specialising in gothic creatures 3D printed in France. Each piece is created with passion by Lubma3D.",
        
        "contact": "For any questions, contact us at lubma3D@outlook.fr. We usually respond within 24-48h.",
        
        "help": "I can help with: shipping, payment, products, materials, sizes, custom orders, engraving, returns, refunds, order tracking, stock, care, discounts, social media, about.",
        
        "default": "I'm sorry, I don't understand. I can help with: shipping, payment, products, returns, tracking, materials, sizes, custom orders, engraving, refunds, stock, care, discounts, social media or contact.",
    },
    "sk": {
        "greeting": "Ahoj! Som Mr.Citrouille, asistent Velvet Creature. Ako vám môžem pomôcť?",
        
        "shipping": "Doručujeme do Francúzska (2-5 dní), Európy (5-10 dní) a medzinárodne (10-20 dní). Objednávky odosielame po 3-7 pracovných dňoch výroby. Spôsoby dopravy: Mondial Relay (výdajné miesta a doručenie domov) a Shop to Shop by Chronopost.",
        
        "payment": "Prijímame platby kartou (Stripe) a bankovým prevodom. Platba je 100% bezpečná a údaje o karte nikdy neukladáme na našich serveroch.",
        
        "products": "Naše produkty sú 3D tlačené z PLA (kyselina polymliečna), PETG alebo TPU. PLA je biologicky rozložiteľné a netoxické, PETG je odolné voči vode a nárazom a TPU je flexibilné a elastické. Každý kus je ručne dokončený a preto jedinečný!",

"materials": "Používame tri materiály: PLA (ekologické a biologicky rozložiteľné), PETG (odolné voči vode a nárazom) a TPU (flexibilné a elastické). Každý materiál má svoje výhody podľa použitia. Každý kus je ručne dokončený.",
        
        "sizes": "Veľkosti sa líšia podľa produktov. Presné rozmery nájdete na stránke každého produktu. Ak potrebujete špecifickú veľkosť, neváhajte nás kontaktovať!",
        
        "custom": "Ponúkame zákazkové objednávky! Môžete požiadať o model na mieru, gravírovanie textu alebo loga. Prejdite na stránku 'Zákazková objednávka' a popíšte svoj projekt.",
        
        "engraving": "Ponúkame gravírovanie textu, loga alebo obrázka na väčšinu našich produktov. Pošlite nám svoj nápad na stránke 'Zákazková objednávka' a my vám pošleme cenovú ponuku!",
        
        "return": "Máte 14 dní na rozmyslenie (právo na odstúpenie podľa článku L221-18 francúzskeho spotrebiteľského zákonníka). Zákazkové produkty nie je možné vrátiť. Pre vrátenie nás kontaktujte na lubma3D@outlook.fr",
        
        "refund": "Vrátenie peňazí sa spracuje do 14 dní po prijatí a kontrole vrátených položiek. Suma sa vracia rovnakým spôsobom platby ako pôvodná transakcia.",
        
        "tracking": "Akonáhle bude vaša objednávka odoslaná, dostanete email s číslom na sledovanie. Objednávky si môžete pozrieť aj vo svojom účte.",
        
        "stock": "Väčšina našich produktov sa tlačí na objednávku. Ak je produkt označený 'Na sklade', je dostupný okamžite. Inak počítajte 3-7 pracovných dní na výrobu.",
        
        "care": "Naše produkty sú krehké. Čistite ich jemne suchou mäkkou handričkou. Vyhnite sa dlhodobému vystaveniu slnku a teplu. Nedávajte ich do vody.",
        
        "discounts": "Aktuálne zľavy nájdete na našich sociálnych sieťach! Pravidelne zverejňujeme exkluzívne ponuky pre našich odberateľov.",
        
        "social": "Nájdete nás na Instagrame a TikToku! Vyhľadajte 'VelvetCreature' a uvidíte naše výtvory a zákulisie.",
        
        "about": "Velvet Creature je remeselná spoločnosť špecializujúca sa na gotické stvorenia tlačené 3D vo Francúzsku. Každý kus je vytvorený s vášňou od Lubma3D.",
        
        "contact": "Pre akékoľvek otázky nás kontaktujte na lubma3D@outlook.fr. Zvyčajne odpovedáme do 24-48h.",
        
        "help": "Môžem pomôcť s: dopravou, platbou, produktmi, materiálmi, veľkosťami, zákazkovými objednávkami, gravírovaním, vrátením, vrátením peňazí, sledovaním objednávky, skladom, starostlivosťou, zľavami, sociálnymi sieťami, o nás.",
        
        "default": "Prepáčte, nerozumiem. Môžem pomôcť s: dopravou, platbou, produktmi, vrátením, sledovaním, materiálmi, veľkosťami, zákazkovými objednávkami, gravírovaním, vrátením peňazí, skladom, starostlivosťou, zľavami, sociálnymi sieťami alebo kontaktom.",
    }
}

# Kľúčové slová pre rozpoznanie otázky
KEYWORDS = {
    "shipping": ["doprava", "livraison", "delivery", "shipping", "doručenie", "expédition", "dodanie", "envoi", "post", "colis", "balík", "doručenie", "kde je", "ou est", "where is"],
    "payment": ["platba", "paiement", "payment", "card", "karta", "carte", "virement", "prevod", "stripe", "bank", "cb", "paypal"],
    "products": ["produkt", "produit", "product", "matériau", "material", "materiál", "pla", "3d", "impression", "tlač", "qualité", "kvalita", "fini", "dokončenie"],
    "materials": ["matériau", "material", "materiál", "pla", "plastique", "plast", "ecolo", "bio", "biodégradable", "rozložiteľný"],
    "sizes": ["taille", "size", "veľkosť", "dimension", "rozmer", "hauteur", "výška", "largeur", "šírka"],
    "custom": ["custom", "personnalis", "zákazk", "sur mesure", "na mieru", "special", "špeciál"],
    "engraving": ["gravure", "engrav", "gravír", "texte", "text", "logo", "image", "obráz"],
    "return": ["retour", "vrátenie", "return", "rembours", "vrátiť", "14 jours", "14 dní", "odstúpenie", "rétractation", "annuler", "zrušiť"],
    "refund": ["rembours", "refund", "vrátenie peňazí", "peniaze", "argent", "money"],
    "tracking": ["suivi", "tracking", "sledovanie", "suivre", "track", "sledovať", "čísle", "numero", "kde je moja", "ou est ma", "where is my"],
    "stock": ["stock", "sklad", "dispo", "dostupn", "en stock", "na sklade", "rupture", "vypredané"],
    "care": ["nettoy", "care", "starostlivosť", "entretien", "čistenie", "clean", "údržb", "fragile", "krehk"],
    "discounts": ["promo", "discount", "zľava", "réduction", "code", "kód", "offre", "ponuka", "soldes", "výpredaj"],
    "social": ["instagram", "tiktok", "facebook", "social", "réseaux", "siete", "follow", "sledovať"],
    "about": ["about", "o vás", "qui", "kto ste", "histoir", "príbeh", "lubma3d", "velvet", "čo je", "qu'est", "what is"],
    "contact": ["contact", "email", "kontakt", "kde", "ou", "where", "nájsť", "trouver", "adresse", "adresa"],
    "help": ["help", "aide", "pomoc", "aider", "pomôcť", "what can", "que peux", "čo môže"],
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