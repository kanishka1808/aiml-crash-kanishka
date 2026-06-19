# day5 task9 --Inventory Management System

import csv


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} | Price: {self.price} | Quantity: {self.quantity}"


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def total_value(self) -> float:
        return sum(product.price * product.quantity for product in self.products)

    def find_product(self, name: str):
        for product in self.products:
            if product.name.lower() == name.lower():
                return product
        return None

    def save_to_csv(self, filename):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(["name", "price", "quantity"])

            for product in self.products:
                writer.writerow(
                    [product.name, product.price, product.quantity]
                )

    def load_from_csv(self, filename):
        self.products = []

        with open(filename, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                product = Product(
                    row["name"],
                    float(row["price"]),
                    int(row["quantity"])
                )

                self.products.append(product)


# Create Inventory
inventory = Inventory()

# Add Products
inventory.add_product(Product("Laptop", 50000, 2))
inventory.add_product(Product("Mouse", 500, 5))
inventory.add_product(Product("Keyboard", 1500, 3))

# Total Value
print("Total Inventory Value:", inventory.total_value())

# Find Product
found = inventory.find_product("mouse")

if found:
    print("Found Product:", found)

# Save to CSV
inventory.save_to_csv("inventory.csv")

# Load from CSV
new_inventory = Inventory()
new_inventory.load_from_csv("inventory.csv")

print("\nProducts Loaded From CSV:")

for product in new_inventory.products:
    print(product)

# Explore :
# load_from_csv could also be implemented as a
# class method that returns a new Inventory object.
# A static method does not receive cls or self.