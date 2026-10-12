
def calculate_total(price, quantity):
    if price < 0 or quantity < 0:
        raise ValueError("Price and quantity must be non-negative")

    return price * quantity


def is_valid_quantity(quantity):
    # Deliberate bug: zero should be a valid quantity.
    return quantity > 0
