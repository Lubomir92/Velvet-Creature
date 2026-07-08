from products.models import Product


def cart_context(request):

    cart = request.session.get("cart", {})

    count = 0
    items = []
    total = 0

    for product_id, qty in cart.items():

        try:
            product = Product.objects.get(id=product_id)

            items.append({
                "product": product,
                "quantity": qty,
                "total_price": product.price * qty
            })

            count += qty
            total += product.price * qty

        except Product.DoesNotExist:
            continue

    return {
        "cart_count": count,
        "cart_items": items,
        "cart_total": total
    }