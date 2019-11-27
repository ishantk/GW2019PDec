# Container Creation in Memory

name = "John"
age = 10
marks = 97.7

print(">> HashCode of name is:", hex(id(name)))
print(">> HashCode of age is:", hex(id(age)))
print(">> HashCode of marks is:", hex(id(marks)))

# name, age and marks are known as Reference Variables
# Reference Variables will hold HashCode of Storage Container

# Update Data in Container
age = 16
print(">> HashCode of age after update is:", hex(id(age)))

# Copy Operation : Reference Copy
myAge = age
print(">> HashCode of myAge is:", hex(id(myAge)))

myAge = 22

print(">> HashCode of age after update is:", hex(id(age)))
print(">> HashCode of myAge after update is:", hex(id(myAge)))

# Reference Copy
myName = name

# Delete Container
del name

# print(">> name is: ",name)
print(">> myName is: ", myName)
print(">> HashCode of myName is:", hex(id(myName)))


