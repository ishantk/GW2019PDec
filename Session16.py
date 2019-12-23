"""
1. Think of an Object
     Restaurant is an Object
        name,phone,address,timings,pricePerPerson,capacity are Attributes of object
"""

# 2. Create Class
class Restaurant:
    pass

# 3. Create Object in Memory
# Restaurant()            # Object Creation -> HashCode of Object is Returned Back
                          # But we are not saving HashCode in any Reference Variable

r1 = Restaurant()       # Object Construction Statement
r2 = Restaurant()       # Object Construction Statement
r3 = r1                 # Reference Copy

print("r1 is:", r1)
print("r2 is:", r2)
print("r3 is:", r3)

# 4. Manage data in Objects

# 4.1. Add Data to Object
r1.name = "John's Coffee Shop"
r1.address = "Redwood Shores"
r1.phone = "+91 99999 88888"
r3.pricePerPerson = 500

r2.name = "Punjabi Tadka"
r2.address = "ABC Street, Asr"
r2.email = "tadka@example.com"

# 4.2 Read Data On Object
print(r1.__dict__)
print(r2.__dict__)
print(r3.__dict__)

# 4.3 Update Data In Object
r3.address = "Country Homes"
r2.email = "p.tadka@gmail.com"

print()

print(r1.__dict__)
print(r2.__dict__)
print(r3.__dict__)

# 4.4 Delete Data In Object
del r1.phone
del r2.email

print()

print(r1.__dict__)
print(r2.__dict__)
print(r3.__dict__)



