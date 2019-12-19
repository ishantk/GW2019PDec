# Object Oriented Programming in Python
# OOPS in Python
"""
    1. Object
        Object is a Multi Value Container
        Which can have lot of data
        Data may be hetro or homo

    2. Class
        Class represents type of Object

    In OOPS, we need to follow Principle of OOPS to Code

   Principle of OOPS
       1. Think of the Object (Name ? Data ?)
       2. Create its Class    (Object Definition)
       3. From the class create Real Objects (In Memory)

   In Computer Science, we need to study requirements for creating a software
   Requirement: We need to create a software which will
                keep the track of orders coming to a restaurant
                Further, which order is given by which customer should be maintained
                We need all the accounting for how much profits we have made


   Identify Objects
   Look for the terms which will have lot of data associated with them !!

   eg: Restaurant
        name
        phone
        address
        timings
        pricePerPerson
        capacity
        .
        ..
        ...

     1. Think of an Object
     Restaurant is an Object
        name,phone,address,timings,pricePerPerson,capacity are Attributes of object

"""


# 2. Create its class
class Restaurant:
    pass            # we have not coded anything in the class -> This means object created will be empty


# 3. Create a Real Object from Class in Memory | Object Construction Statement
r1 = Restaurant()
# r1 is a reference variable which can be any name of your choice

# print(type(r1))
# print(hex(id(r1)))

# Printing Reference Variable will show is the tye and HashCode of Object
print(r1)
print(r1.__dict__)

# Write Data In Object
r1.name = "Johns Coffee Shop"
r1.phone = "+91 99999 77777"
r1.address = "Redwood Shores"
r1.pricePerPerson = 500
r1.capacity = 100

# Read Data from Object
print(r1.__dict__)

# Update Data In Object
r1.phone = "+91 90909 11010"

print(r1.__dict__)

# Delete Data from Object
del r1.pricePerPerson
del r1.capacity

# Re-Add new Data Anytime :)
r1.email = "johns.coffee@example.com"

print(r1.__dict__)

# Delete Object from Memory
# del r1
# print(r1.__dict__) # error


