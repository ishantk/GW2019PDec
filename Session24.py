# Open a file
# Session23.py in read mode
file = open("Session23.py", "r")
print(file)
print(type(file))

fileContents = file.read()
print(fileContents)
print(type(fileContents))

print("Re-Reading the file")

fileContents = file.read()
print(fileContents)         # File once read cannot be re-read

# Close the file if you do not use it further
# release memory resources
file.close()
print("Is File Closed?", file.closed)
