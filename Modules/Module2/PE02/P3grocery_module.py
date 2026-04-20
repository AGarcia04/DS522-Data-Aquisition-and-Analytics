"""
DS 522 - Programming Exercise 02
Part 3: Grocery Delivery — Module
"""

def add_order(item, quantity, *args):
    """
    Creates a grocery delivery order.

    Parameters:
        item (str)     : Name of the grocery item
        quantity (int) : Number of units
        *args          : Extra delivery info (customer, address, time, notes...)

    Returns:
        dict: Order dictionary
    """
    order = {
        "item": item,
        "quantity": quantity,
        "delivery_info": list(args)
    }
    return order


def display_order(order):
    """Prints a formatted summary of an order."""
    labels = ["Customer", "Address", "Delivery Time", "Notes"]
    print(f"  Item     : {order['item']}")
    print(f"  Quantity : {order['quantity']}")
    for i, info in enumerate(order["delivery_info"]):
        label = labels[i] if i < len(labels) else f"Extra {i + 1}"
        print(f"  {label:<15}: {info}")


def display_all_orders(orders):
    """Prints all orders with numbering."""
    print("\n===== TODAY'S GROCERY DELIVERY ORDERS =====")
    for i, order in enumerate(orders, start=1):
        print(f"\nOrder #{i}")
        display_order(order)
    print("\n============================================")