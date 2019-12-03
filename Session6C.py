# Operators
# Bitwise Operators
# &, |, ^, >>, <<

a = 12                      # 1 1 0 0
print(bin(a))
b = 8                       # 1 0 0 0
print(bin(b))
c = a & b                   # 1 0 0 0
print(">> c is:", c)        # 8

d = a | b
print(">> d is:", d)        # 1 1 0 0

# Number is divided by 2 power 3
e = a >> 3                  # 1 1 0 0 -> _ _ _ 1 -> 0 0 0 1

print(">> e is:", e)

# Number is multiply by 2 power 3
f = a << 3                  # 1 1 0 0 _ _ _ -> 1 1 0 0 0 0 0
print(">> f is:", f)

n1 = 11             # 1 0 1 1 -> _ _ 1 0 -> 0 0 1 0
n1 = n1 >> 2
print(">> n1 is:", n1)

n2 = -11            # 1 0 1 1 -> 0 1 0 0
                    #                  1 -> 0 1 0 1
                    # 0 1 0 1 >> 2 -> 1 1 0 1
                    #                 0 0 1 0
                    #                       1
                    #                 0 0 1 1
n2 = n2 >> 2
print(">> n2 is:", n2) # -3


