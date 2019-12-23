"""
1. Think of an Object
     Restaurant is an Object
        name,phone,address,timings,pricePerPerson,capacity are Attributes of object
"""

# 2. Create Class
class Restaurant:

    # CONSTRUCTOR
    # __init__ is a function and self is an input
    # it is a special function : it must take 1 input at any cost
    # it will be executed automatically when object will be created
    # self will thereafter have the hashcode of that newly created object
    """
    def __init__(self):
        print("---------init started----------")
        print(self)
        print(type(self))
        print("---------init finished----------")
    """
    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address
        self.rating = 3.5

    def showRestaurant(self):
        print("*****************************")
        print("Name\t", self.name)
        print("Phone\t", self.phone)
        print("*****************************")



# 3. Create Object in Memory
# Restaurant()            # Object Creation -> HashCode of Object is Returned Back
                          # But we are not saving HashCode in any Reference Variable

r1 = Restaurant("John's Coffee Shop", "+91 99999 88888", "Redwood Shores")       # Object Construction Statement
r2 = Restaurant("Punjabi Tadka", "+91 999999 777777", "Country Homes")       # Object Construction Statement
r3 = r1                 # Reference Copy

"""
print("r1 is:", r1.__dict__)
print("r2 is:", r2.__dict__)
print("r3 is:", r3.__dict__)

print()

r1.pricePerPerson = 500
del r1.phone

print("r1 is:", r1.__dict__)
print("r2 is:", r2.__dict__)
print("r3 is:", r3.__dict__)
"""

r1.showRestaurant()
r2.showRestaurant()
r3.showRestaurant()


# task : create functions : Add, Delete, Update and Read (show)

