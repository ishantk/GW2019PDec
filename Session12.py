# LIST
# A = [1, 2, 3, 4, 5, 1, 3]
# print("A is:", A, " and type is:", type(A))

# SET
# A = {1, 2, 3, 4, 5, 1, 3}
# print("A is:", A, " and type is:", type(A))

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A)
print(B)

print()

# Union Operation
C = A | B # IMMUTABLE
print(A)
print(C)

# Intersection Operation
D = A & B
print(D)
print(len(D))

# Difference Operation
E = A - B
print(E)