# Import the module created in a separate file
import shopping_module

# Use functions from the imported module
shopping_module.add_items("apples")
shopping_module.add_items("bread", "milk", "eggs", "butter")
shopping_module.add_items('ink', 'backpack', 'pens', 'notebook', 'white paper')

# Print all items in the cart
shopping_module.print_cart()