class Order:
    def __init__(self, customer, order_id=None):
        self.customer = customer
        self.order_id = order_id
        self.products = []
        self.total = 0

    def add_product(self, product, quantity):
        self.products.append((product, quantity))

    def calculate_total(self):
        self.total = sum(product.price * quantity for product, quantity in self.products)
        return self.total

    def generate_summary(self):
        summary = f"Order ID: {self.order_id}\n" \
                  f"Customer: {self.customer.name}\n" \
                  f"Products:\n"
        for product, quantity in self.products:
            summary += f"  - {product.name} (Qty: {quantity}), Price: Rs{product.price}\n"
        summary += f"Total: Rs{self.total}"
        return summary
