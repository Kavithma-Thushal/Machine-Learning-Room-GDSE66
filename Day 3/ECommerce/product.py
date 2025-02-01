class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_details(self):
        return f"Product: {self.name}, Price: Rs{self.price}, Quantity: {self.quantity}"

    def update_price(self, new_price):
        self.price = new_price

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
