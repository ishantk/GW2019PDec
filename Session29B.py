# Single Computation OR Single Expression Evaluation
def areaOfCircle(radius=2):
    area = 3.14 * radius * radius
    return area


result = areaOfCircle()
print(">> result is:",result)

result = areaOfCircle(3.3)
print(">> result with 3.3 is:", result)

# Reference Copy Operation
area = areaOfCircle

print(area)
print(areaOfCircle)

result = area(4.4)
print(">> result with 4.4 is:", result)

# For Single Computation OR Single Expression Evaluation
# Use Lambdas in Python

lRef1 = lambda radius=2: 3.14 * radius * radius
print(lRef1)

result = lRef1(5.5)
print(">> result with 5.5 is:", result)

lRef2 = lambda x, y : x ** y
print(">> 2 power 4 is:", lRef2(2, 4))

lRef3 = lambda x=int(input("Enter X:")), y=int(input("Enter Y:")): x+lRef1(2) ** y
print(lRef3())

