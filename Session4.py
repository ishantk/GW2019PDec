# Value Vs Reference
# Mutablility Vs Immutability

age = 10
# 10 is Data or Literal or Value
# age is storage container which points to data 10
# So, we say age is a Reference Variable and it will hold HashCode of 10

print("age is:", age)
print(">> HashCode for age is:", hex(id(age)))

age = 20

print()

print("age now is:", age)
print(">> HashCode for age now is:", hex(id(age)))

print(">> Type of age is:", type(age))

