names = ["anna", "Bob", "Jennie", "Sia", "Kim"]
ages = [10, 20, 30, 40, 50]

print(len(names))
print(len(ages))

print()

# ASCII Based
print(max(names))
print(min(names))

print()

print(max(ages))
print(min(ages))

print()

# Iterate in List

# for i in range(0, len(names)):
# for i in range(len(names)): # By default will start from 0
for i in range(0, len(names), 2):
    # print(i)
    print(names[i])


# Iterate in List in a Reverse Range Function | Kim to anna

print()

# Enhanced For Loop
for name in names:
    print(name)

