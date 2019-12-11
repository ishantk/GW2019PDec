
"""
# cart is an empty list
cart = []
foodItem = input("Enter Food Item of your Choice: ")

cart.append(foodItem)
print(">> Your Cart is:", cart)

print()

foodItem = input("Enter Food Item of your Choice: ")

cart.append(foodItem)
print(">> Your Cart is:", cart)
"""

# cart is an empty list
cart = []

choice = "yes"

while choice == "yes":

    foodItem = input("Enter Food Item of your Choice: ")
    cart.append(foodItem)

    choice = input("Add Another Food Item (yes/no): ")

print(">> Your Final Cart is:", cart)