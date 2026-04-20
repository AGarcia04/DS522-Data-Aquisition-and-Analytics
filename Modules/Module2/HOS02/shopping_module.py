# Initialize the cart as a global variable
cart = []

def add_items(*items):
    """Add items to the shopping cart."""
    global cart
    for item in items:
        cart.append(item)

def print_cart():
    """Print all items in the shopping cart."""
    print("Items in the cart:", cart)