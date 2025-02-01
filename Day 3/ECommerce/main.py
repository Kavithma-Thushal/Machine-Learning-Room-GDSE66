from product import Product
from customer import Customer
from order import Order
from inventory import Inventory


class ECommerce:
    def __init__(self):
        self.customers = []
        self.inventory = Inventory()
        self.products = []
        self.orders = []

    def main_menu(self):
        while True:
            print("\n--- E-Commerce Management System ---")
            print("1. Product Management")
            print("2. Customer Management")
            print("3. Inventory Management")
            print("4. Order Management")
            print("5. Exit")
            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                self.product_menu()
            elif choice == '2':
                self.customer_menu()
            elif choice == '3':
                self.inventory_menu()
            elif choice == '4':
                self.order_menu()
            elif choice == '5':
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1-5.")

    def customer_menu(self):
        while True:
            print("\n--- Customer Management ---")
            print("1. Add Customer")
            print("2. Update Customer")
            print("3. Delete Customer")
            print("4. View Customers")
            print("5. Back")
            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                name = input("Enter customer name: ")
                address = input("Enter customer address: ")
                contact = input("Enter customer contact: ")
                new_customer = Customer(name, address, contact)
                self.customers.append(new_customer)
                print("Customer added successfully!")
            elif choice == '2':
                if not self.customers:
                    print("No customers available to update.")
                    continue
                for i, c in enumerate(self.customers, 1):
                    print(f"{i}. {c.get_details()}")
                index = int(input("Enter customer number to update: ")) - 1
                if 0 <= index < len(self.customers):
                    customer = self.customers[index]
                    print("1. Update Address\n2. Update Contact")
                    update_choice = input("Enter choice: ")
                    if update_choice == '1':
                        new_address = input("Enter new address: ")
                        customer.address = new_address
                    elif update_choice == '2':
                        new_contact = input("Enter new contact: ")
                        customer.contact = new_contact
                    print("Customer updated successfully!")
            elif choice == '3':
                if not self.customers:
                    print("No customers to delete.")
                    continue
                for i, c in enumerate(self.customers, 1):
                    print(f"{i}. {c.get_details()}")
                index = int(input("Enter customer number to delete: ")) - 1
                if 0 <= index < len(self.customers):
                    del self.customers[index]
                    print("Customer deleted successfully!")
            elif choice == '4':
                for c in self.customers:
                    print(c.get_details())
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please enter a number between 1-5.")

    def inventory_menu(self):
        while True:
            print("\n--- Inventory Management ---")
            print("1. Add Product to Inventory")
            print("2. Remove Product from Inventory")
            print("3. Check Stock")
            print("4. Back")
            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                if not self.products:
                    print("No products available to add to inventory.")
                    continue
                print("Select Product:")
                for i, p in enumerate(self.products, 1):
                    print(f"{i}. {p.get_details()}")
                product_index = int(input("Enter product number: ")) - 1
                product = self.products[product_index]
                self.inventory.add_product(product)
                print("Product added to inventory successfully!")
            elif choice == '2':
                product_name = input("Enter product name: ")
                quantity = int(input("Enter quantity: "))
                self.inventory.remove_product(product_name, quantity)
            elif choice == '3':
                product_name = input("Enter product name: ")
                stock = self.inventory.check_stock(product_name)
                print(f"Stock for {product_name}: {stock}")
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please enter a number between 1-4.")

    def product_menu(self):
        while True:
            print("\n--- Product Management ---")
            print("1. Add Product")
            print("2. Update Product")
            print("3. Delete Product")
            print("4. View Products")
            print("5. Back")
            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                name = input("Enter product name: ")
                price = float(input("Enter product price: "))
                quantity = int(input("Enter product quantity: "))
                new_product = Product(name, price, quantity)
                self.products.append(new_product)
                print("Product added successfully!")
            elif choice == '2':
                if not self.products:
                    print("No products available to update.")
                    continue
                for i, p in enumerate(self.products, 1):
                    print(f"{i}. {p.get_details()}")
                index = int(input("Enter product number to update: ")) - 1
                if 0 <= index < len(self.products):
                    product = self.products[index]
                    print("1. Update Price\n2. Update Quantity")
                    update_choice = input("Enter choice: ")
                    if update_choice == '1':
                        new_price = float(input("Enter new price: "))
                        product.update_price(new_price)
                    elif update_choice == '2':
                        new_quantity = int(input("Enter new quantity: "))
                        product.update_quantity(new_quantity)
                    print("Product updated successfully!")
            elif choice == '3':
                if not self.products:
                    print("No products to delete.")
                    continue
                for i, p in enumerate(self.products, 1):
                    print(f"{i}. {p.get_details()}")
                index = int(input("Enter product number to delete: ")) - 1
                if 0 <= index < len(self.products):
                    del self.products[index]
                    print("Product deleted successfully!")
            elif choice == '4':
                for p in self.products:
                    print(p.get_details())
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please enter a number between 1-5.")

    def order_menu(self):
        while True:
            print("\n--- Order Management ---")
            print("1. Create Order")
            print("2. View Orders")
            print("3. Back")
            choice = input("Enter your choice (1-3): ")

            if choice == '1':
                if not self.customers or not self.products:
                    print("Need customers and products first.")
                    continue
                print("Select Customer:")
                for i, c in enumerate(self.customers, 1):
                    print(f"{i}. {c.get_details()}")
                customer_index = int(input("Enter customer number: ")) - 1
                customer = self.customers[customer_index]
                order = Order(customer, len(self.orders) + 1)
                while True:
                    print("Select Product:")
                    for i, p in enumerate(self.products, 1):
                        print(f"{i}. {p.get_details()}")
                    product_index = int(input("Enter product number (0 to finish): ")) - 1
                    if product_index == -1:
                        break
                    quantity = int(input("Enter quantity: "))
                    order.add_product(self.products[product_index], quantity)
                order.calculate_total()
                self.orders.append(order)
                print("Order created successfully!")
            elif choice == '2':
                for order in self.orders:
                    print(order.generate_summary())
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please enter a number between 1-3.")


def main():
    system = ECommerce()
    system.main_menu()


if __name__ == "__main__":
    main()
