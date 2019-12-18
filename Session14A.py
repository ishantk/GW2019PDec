# Default Arguments
def addNumbers(num1=0, num2=0):
    sum = num1 + num2
    # return sum
    print("Sum of", num1, "and", num2, "is:", sum)


print(">> addNumbers is:", addNumbers)

# ReCreating same Function again will delete old function from memory

# def addNumbers(num1=0, num2, num3): # error : default values must be given from Right to left
# def addNumbers(num1=0, num2, num3=0): # error

# def addNumbers(num1=1, num2=2, num3=3):
def addNumbers(num1, num2=2, num3=3):
    sum = num1 + num2 + num3
    print("Sum of", num1, "and", num2, "and", num3, "is:", sum)


print(">> addNumbers now is:", addNumbers)

addNumbers(10, 20, 30)
addNumbers(10, 20)
addNumbers(11, 33)

addNumbers(11)
addNumbers()

# As of now addNumbers can take only 3 inputs
# addNumbers(1, 2, 3, 4, 5, 6)
# addNumbers(1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10)

