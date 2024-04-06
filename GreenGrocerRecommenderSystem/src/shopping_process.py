class ShoppingProcess:
    def __init__(self, inventory, customer_interaction):
        self.inventory = inventory
        self.customer_interaction = customer_interaction

    def start_shopping(self):
        customer_name = self.customer_interaction.greet_customer()
        customer_id = self.customer_interaction.assign_id(customer_name)
        while True:
            item = input("What item do you need? (Type 'exit' to quit): ")
            if item == 'exit':
                print("Thank you for visiting. Goodbye!")
                break
            if self.inventory.check_stock(item):
                print(f"{item.capitalize()} is in stock. Please proceed to the counter.")
            else:
                print(f"Unfortunately, {item.capitalize()} is out of stock. Thank you for coming.")
                break

        print("Thank you for shopping with GreenGrocer!")
