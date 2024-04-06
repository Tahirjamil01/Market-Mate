class Inventory:
    def __init__(self):
        self.items = {
            'bread': 50,
            'milk': 30,
            'eggs': 100,
            'apples': 200
        }

    def check_stock(self, item_name):
        return self.items.get(item_name, 0) > 0

    def update_stock(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] -= quantity
            if self.items[item_name] < 0:
                self.items[item_name] = 0
        else:
            print(f"Item '{item_name}' not found in inventory.")
