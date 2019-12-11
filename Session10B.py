cart = []

# add data in the end
cart.append("Shoes")
cart.append("Shirt")
cart.append("Watch")

print(cart)

# Add another list in the same list
cart.extend(["Jeans", "Bottle"])

print(cart)

# Add the data in Between
cart.insert(1, "Napkins")

print(cart)

# Remove the 2nd index
cart.pop(2)
print(cart)

# Assignment : With inputs from user
#              design a shopping cart