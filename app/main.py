
def calculate_total(price, quantity):
    if price < 0 or quantity < 0:
        raise ValueError("Price and quantity must be non-negative")

    return price * quantity


def is_valid_quantity(quantity):
    return quantity >= 0


def calculate_discount(price, discount_percent):
    if price < 0:
        raise ValueError("Price must be non-negative")

    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount must be between 0 and 100")

    # Deliberate bug: returns the discount amount,
    # instead of the final price after discount.
    return price * discount_percent / 100


if __name__ == "__main__":
    print(calculate_total(100, 2))
