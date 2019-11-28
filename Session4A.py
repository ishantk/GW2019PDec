# Multi Value Container

# TUPLE IS IMMUTABLE
# johnMarks = (90, 75, 95)
# fionnaMarks = 80, 85, 85

# LIST IS MUTABLE
johnMarks = [90, 75, 95]
fionnaMarks = [80, 85, 85]

print(">> johnMarks is:", johnMarks, hex(id(johnMarks)))
print(">> fionnaMarks is:", fionnaMarks, hex(id(fionnaMarks)))

print(">> type of johnMarks is:", type(johnMarks))
print(">> type of fionnaMarks is:", type(fionnaMarks))

# Reading Data from Tuple
print(johnMarks[0])     # 90
print(fionnaMarks[0])   # 80

# Update Data in Tuple
# johnMarks[0] = 99     #Error in Tuple
johnMarks[0] = 99       #OK

print("=====")

# Read All
for elm in johnMarks:
    print(elm)

print("=====")
for elm in fionnaMarks:
    print(elm)