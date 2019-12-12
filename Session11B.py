name = "Fionna"
age = 30

# String Formatting
print(">> Welcome", name, "to our organization !!")
print(">> Good to know that you are ", age, "years old")

print(">> Welcome %s ! You are %d years old !!" % (name, age))
print(">> Welcome {} ! You are {} years old !!".format(name, age))

number = 7
for i in range(1, 11):
    print("{} {}'s are {}".format(number, i, (number*i)))