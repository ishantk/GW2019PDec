dish1 = {"name": "Dal Makhani", "price": 100}
dish2 = {"name": "Paneer Tikka", "price": 200}
dish3 = {"name": "Noodles", "price": 150}

# print(dish1)
# print(dish2)
# print(dish3)

# List of Dictionaries :)
dishes = [dish1, dish2, dish3]

# for i in range(0, len(dishes)):
#     print(dishes[i])

for dish in dishes:
    # print(dish)
    # print(dish["name"], dish["price"])
    print("=========================")
    print(dish["name"], "\t \u20b9", dish["price"])
    print("=========================")
    print()

# Create a Menu List which shall show dishes
# Ask user to add dishes in a cart
# finally, show user the amount in total and ask him to apply promo code on total amount
