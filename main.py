from inventory import Inventory
from customer_interaction import CustomerInteraction
from shopping_process import ShoppingProcess

if __name__ == "__main__":
    inventory = Inventory()
    customer_interaction = CustomerInteraction()
    shopping_process = ShoppingProcess(inventory, customer_interaction)
    shopping_process.start_shopping()
