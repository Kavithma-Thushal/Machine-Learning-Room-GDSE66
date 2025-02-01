class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.name in self.products:
            self.products[product.name].quantity += product.quantity
        else:
            self.products[product.name] = product

    def remove_product(self, product_name, quantity):
        if product_name in self.products:
            if self.products[product_name].quantity >= quantity:
                self.products[product_name].quantity -= quantity
            else:
                print(f"Insufficient stock for {product_name}")
        else:
            print(f"Product '{product_name}' not found in inventory.")

    def check_stock(self, product_name):
        return self.products.get(product_name, 0).quantity if product_name in self.products else 0
