import os

print(os.getcwd())
print(os.name)
print(os.uname())
print(os.getlogin())
print(os.getppid())

pathToDir = "/Users/ishantkumar/Downloads"
pathToFile = "/Users/ishantkumar/Downloads/orders-19jan2020.csv"

print("Is Downloads Directory available?", os.path.exists(pathToDir))
print("Is orders-19jan2020.csv available?", os.path.exists(pathToFile))

# path = "/Users/ishantkumar/Downloads/Hello"
# os.mkdir(path)
# os.rmdir(path)

path = "/Users/ishantkumar/Downloads"
files = os.walk(path)

for file in files:
    print(file)

# File Explorer
# Documents | Images | Videos | Audios

