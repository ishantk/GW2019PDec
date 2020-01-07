file = open("Session23.py", "r")
# Read first 15 characters
data = file.read(15)

print(data)

# Read next 30 characters after 15 characters
data = file.read(30)
print(data)

file.close()    # Release memory Resources

