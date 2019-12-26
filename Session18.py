# HAS-A Relationship
# Customer HAS-An Address | 1 to 1
# Category HAS Products   | 1 to many
# many to many

# 1. Think of an Object
#     Address : adrsLine, city, state, zipCode
#     Customer : name, phone, email, address

class Address:

    # Constructor __init__
    # why we created constructor ?
    # to have standardization in object construction
    def __init__(self, adrsLine, city, state, zipCode):
        # LHS: self.adrsLine is attribute of object
        # RHS: adrsLine is value which is copied into attribute
        self.adrsLine = adrsLine
        self.city = city
        self.state = state
        self.zipCode = zipCode

    def showAddress(self):
        print("--------------------------")
        print("{} | {}".format(self.adrsLine, self.city))
        print("{} | {}".format(self.state, self.zipCode))
        print("--------------------------")


class Customer:

    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def showCustomer(self):
        print("======================")
        print("{} | {} | {}".format(self.name, self.phone, self.email))
        # self.address.showAddress()

        # for adrs in self.address:
        #     adrs.showAddress()

        for i in range(0, len(self.address)):
            self.address[i].showAddress()


"""
aRef1 = Address("Redwood Shores", "Ludhiana", "Punjab", 141002)
aRef2 = Address("Pristine Magnum", "Ludhiana", "Punjab", 141004)

print(">> aRef1 is:", aRef1)
print(">> aRef2 is:", aRef2)

# aRef1.showAddress()
# aRef2.showAddress()

cRef1 = Customer("John", "+91 99999 88888", "john@example.com", aRef1)
cRef2 = Customer("Fionna", "+91 77777 88888", "fionna@example.com", aRef2)

print(">> cRef1 is:", cRef1)
print(">> cRef2 is:", cRef2)

cRef1.showCustomer()
cRef2.showCustomer()
"""

aRef1 = Address("Redwood Shores", "Ludhiana", "Punjab", 141002)
aRef2 = Address("Pristine Magnum", "Ludhiana", "Punjab", 141004)

addresses = [aRef1, aRef2]

cRef1 = Customer("John", "+91 99999 88888", "john@example.com", addresses)
cRef1.showCustomer()

"""
    Restaurant HAS-A Menu | 1 to 1
    Menu Has Categories | 1 to many
    Category Has Dishes | 1 to many
    
    
    Restaurant
    Menu
    Category
    Dish
    
"""
