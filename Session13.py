# Functions
# is a module which will
# help to execute certain set of instructions
# again and again as in when required
"""
    y = a x*x + b

"""
"""
a = 10
b = 20

x = int(input("Enter Value of X:"))

y = a * (x*x) + b

print(">> Y is:",y)

print()


x = int(input("Enter Value of X:"))

y = a * (x*x) + b

print(">> Y is:",y)
"""

def eqn(a, b, x):
    y = a * (x * x) + b
    return y    # return must be last statement


# output = eqn(10, 20, 5)
# print(">> Output is: ",output)

print(">> Output is: ",eqn(10, 20, 5))
print(">> Output is: ",eqn(11, 21, 5))
print(">> Output is: ",eqn(12, 22, 5))
print(">> Output is: ",eqn(13, 23, 5))
print(">> Output is: ",eqn(14, 24, 5))


