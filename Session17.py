"""
1. Think of an Object
Object      : Dish
Attributes  : name, price, rating, description, quantity

"""

# 2. Create its class
# class represents type of Object

class Dish:

    # Constructor : Whenever Object will be created in memory, constructor will be executed
    # self        : is a reference variable which is input to constructor
    #             : will have hash code of object
    # Inputs      : Let all the attributes if an object be inputs
    def __init__(self, name, price, rating, description, q):
        print(">> __init__ executed. self is:",self)
        self.name = name
        self.price = price
        self.rating = rating
        self.description = description
        self.quantity = q


    def show(self):
        print("------------------------------------")
        print(self.name, "\t\t", self.quantity)
        print("Rating:", self.rating)
        print("Price:", self.price)
        print(self.description)
        print("------------------------------------")

    def showTotal(self, d2, d3):
        totalItems = self.quantity + d2.quantity + d3.quantity
        totalPrice = self.quantity * self.price + d2.quantity * d2.price + d3.quantity * d3.price
        print("------------------------")
        print("Total Items:",totalItems)
        print("Total Price:",totalPrice)
        print("------------------------")



# dish1 = Dish("Veg Thali", 185, 4.5, "Special Veg Thali by Basant", 1)
# print()
#
# dish2 = Dish("Dal Makhani", 180, 4.5, "Black Lentils Cooked Overnight", 2)
# print()
#
# dish3 = Dish("Kadai Paneer", 265, 5, "Special Paneer in Tomato Capsicum w/wo Gravy", 1)
# print()

#
# print(dish1)
# print(dish1.__dict__)
#
# print()
#
# print(dish2)
# print(dish2.__dict__)
#
# print()
#
# print(dish3)
# print(dish3.__dict__)

# dish1.show()
# dish2.show()
# dish3.show()
#
# totalItems = dish1.quantity + dish2.quantity + dish3.quantity
# totalPrice = dish1.quantity*dish1.price + dish2.quantity*dish2.price + dish3.quantity*dish3.price
#
# print("------------------------")
# print("Total Items:",totalItems)
# print("Total Price:",totalPrice)
# print("------------------------")

dish1 = Dish("Veg Thali", 185, 4.5, "Special Veg Thali by Basant", 1)
dish2 = Dish("Dal Makhani", 180, 4.5, "Black Lentils Cooked Overnight", 2)
dish3 = Dish("Kadai Paneer", 265, 5, "Special Paneer in Tomato Capsicum w/wo Gravy", 1)

# List of References to Objects
# dishes = [dish1, dish2, dish3]
#
# totalItems = 0
# totalPrice = 0
# for dish in dishes:
#     totalItems = totalItems + dish.quantity
#     totalPrice = totalPrice + (dish.quantity*dish.price)
#
# print("------------------------")
# print("Total Items:",totalItems)
# print("Total Price:",totalPrice)
# print("------------------------")

# dish1.showTotal(dish2, dish3)

cart = []
cart.append(dish1)

# Assignment : implement Shopping Cart

