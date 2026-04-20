"""
DS 522 - Programming Exercise 02
Part 3: Grocery Delivery — Main Script
"""

import P3grocery_module as gm

# Create orders using the module's add_order function
order1 = gm.add_order("Apples", 6, "Maria Lopez", "123 Maple St", "10:00 AM", "Leave at door")
order2 = gm.add_order("Bread", 2, "John Smith", "456 Oak Ave", "1:30 PM")
order3 = gm.add_order("Milk", 1, "Sara Chen", "789 Pine Rd", "3:00 PM", "Ring doorbell")

# Collect all orders
orders = [order1, order2, order3]

# Display all orders
gm.display_all_orders(orders)