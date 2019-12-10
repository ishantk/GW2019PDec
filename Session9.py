"""

    MODEL
        Data
        sourceLocation, destinationLocation, typeOfCab

    VIEW
        UI (User Interfaces containing Views and Widgets to interact)
        Where either we show data to User or User inputs the data

    CONTROLLER
        Logic
            1. Computation
            2. Conditional Flows
            3. Loops/Iterations


    **>>
    Sequences in Python (Built In Data Structures)
    Data Structure is a way to store data in memory
        1. List
        2. Tuple
        3. String
        4. Set
        5. Dictionary


    **>> Operations
        1. Concatenation
        2. Repetition
        3. Membership Testing
        4. Indexing
        5. Slicing

"""

# 1. List in Python
#                    0                      1               2
remoteControls = ["ps-controller1", "ps-controller2", "xb-controller3"]
remoteControlPrices = [200, 500, 700]
names = ["John", "Jennie", "Jack"]

print(remoteControls, type(remoteControls))
print(names, type(names))

# 1. Concatenation
#    Add 2 lists i.e. Merge Data of 2 lists and create a new list
newNames = names + ["Fionna", "Kim"]
print(names) # This will not change
print(newNames) # This is a new list in memory

print()

# 2. Repetition
repeatedNames = names * 3
print(names)
print(repeatedNames)

# 3. Membership Testing
print("Leo" in names)
print("Leo" not in names)

# 4. Indexing
print(names[1])
print(newNames[4])
print(len(newNames))
print(newNames[-1])   # Negative Index(Start from Last)


# 5. Slicing
print(newNames[1:4])    # 1 inclusive and 4 not inclusive
print(newNames[2:])     # 2 inclusive till the end
print(newNames[:3])     # 0 till less than 3
print("::", newNames[-1:-3]) # ?
print("::", newNames[-1:3])  # ?
print("::", newNames[3:-1])  # ?
print("::", newNames[:])

# Write a slice which will give reverse of list
