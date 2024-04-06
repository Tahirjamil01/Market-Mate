class CustomerInteraction:
    def __init__(self):
        self.customers = {}
        self.last_id = 0

    def greet_customer(self):
        print("Welcome to the Grocery Store!")
        customer_name = input("Please enter your name: ")
        return customer_name

    def assign_id(self, customer_name):
        self.last_id += 1
        self.customers[self.last_id] = customer_name
        print(f"Hello, {customer_name}! Your customer ID is {self.last_id}.")
        return self.last_id
