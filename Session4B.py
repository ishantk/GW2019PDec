johnMarks = [90, 75, 95]

# reference copy : Copied the HashCode
fionnaMarks = johnMarks

# 1. Change Data in fionnaMarks
# 2. Check if it changes in johnMarks
# 3. Create Memory Representation


print("johnMarks is:", johnMarks, hex(id(johnMarks)))
print("fionnaMarks is:", fionnaMarks, hex(id(fionnaMarks)))

print(">>>>>>>>>>>>>>>>>>>>>")

print(">> johnMarks[0] is:", johnMarks[0], hex(id(johnMarks[0])))
print(">> johnMarks[1] is:", johnMarks[1], hex(id(johnMarks[1])))
print(">> johnMarks[2] is:", johnMarks[2], hex(id(johnMarks[2])))

print(">> fionnaMarks[0] is:", fionnaMarks[0], hex(id(fionnaMarks[0])))
print(">> fionnaMarks[1] is:", fionnaMarks[1], hex(id(fionnaMarks[1])))
print(">> fionnaMarks[2] is:", fionnaMarks[2], hex(id(fionnaMarks[2])))

print(">>>>>>>>>>>>>>>>>>>>>")

fionnaMarks[1] = 55

print(johnMarks[1])

print(">> johnMarks[0] is:", johnMarks[0], hex(id(johnMarks[0])))
print(">> johnMarks[1] is:", johnMarks[1], hex(id(johnMarks[1])))
print(">> johnMarks[2] is:", johnMarks[2], hex(id(johnMarks[2])))

print(">> fionnaMarks[0] is:", fionnaMarks[0], hex(id(fionnaMarks[0])))
print(">> fionnaMarks[1] is:", fionnaMarks[1], hex(id(fionnaMarks[1])))
print(">> fionnaMarks[2] is:", fionnaMarks[2], hex(id(fionnaMarks[2])))

