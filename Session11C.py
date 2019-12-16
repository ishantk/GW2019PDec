# built In Functions on Strings
# Strings are IMMUTABLE (They Cannot be Changed)
# Any manipulation operation on strings will create a new String in memory
name = "Fionna Flynn"
name1 = name.upper()
print(">> Name is:", name)
print(">> Name1 is:", name1)

name2 = "john watson"
name3 = name2.capitalize()
print(">> Name3 is:", name3)


names = "John, Jennie, Jim, Jack, Joe"
print(len(names))               # 28
print(names[len(names)-1])      # e

# idx = names.index("h")
idx = names.index("Jennie")
print(">> idx is:", idx)

moreNames = names.replace("J", "K")
print(names)
print(moreNames)

allNames = names.split(",")
print(allNames)
for n in allNames:
    print(n.strip())  # strip eliminates white spaces front and end

ipAddress = "198.10.12.1"
count = 0
for i in range(len(ipAddress)):
    if ipAddress[i] == ".":
        count = count + 1

print(">> . occurs {} times".format(count))

num = ipAddress.count(".", 0, len(ipAddress))
print(">> num is:", num)

quote = "Search the Candle, rather than cursing the darkness"
words = quote.split(" ")
print(words, len(words))

salutation = "Mr."
fname = "John"
lname = "Watson"

fullName = salutation + " " + fname + " " + lname
print(fullName)

number = "100"
print(number.isdigit())
# number.is expore .is functions

songName = "hello.mp3"
if songName.endswith(".mp3"): # startsWith
    print(">> We can play the song")

# WAP to create a function count
"""
def count(findIn, findWhat, from, to):
    

    ipAddress = "198.10.12.1"
    print(count(ipAddress, ".", 0, len(ipAddress))) : 3
         
"""


