class Customer:
    def __init__(self, name, address, contact):
        self.name = name
        self.address = address
        self.contact = contact

    def get_details(self):
        return f"Name: {self.name}, Address: {self.address}, Contact: {self.contact}"
