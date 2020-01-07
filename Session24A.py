# file = open("/users/ishantkumar/Downloads/AnyName.java", "r")
file = open("Session23.py", "r")
# fileContent = file.read() # Read All
# print(fileContent)

# line = file.readline()
# print(line)
#
# line = file.readline()
# print(line)


lines = file.readlines()    # we will now get lines in the file in the form of list
print(lines)
print(type(lines))


for line in lines:
    print(line)

print("Lines:", len(lines))

# Assignment : Find how many lists are created in Session23.py by reading it line by line. Use String API's as taught earlier