name = "John Watson"
print(name, type(name), hex(id(name)))
print(len(name))
print("Max: ", max(name)) # t
print("Min: ", min(name)) #

# Indexing
print(name[1])            # o
print(name[len(name)-1])  # n
print(name[1:4])          # ohn

# Membership Testing
print('n' in name)
print('ohn' in name)
print('taW' not in name)

# Validations
email = input("Enter Your Email: ")
password = input("Enter Password: ")

if '@' in email and '.' in email:
    print(">> Valid Email")
else:
    print(">> Please enter a valid email")

if len(password) < 6:
    print(">> Enter a Password greater than or equal to 6 characters")
else:
    print(">> Valid Password")
