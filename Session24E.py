class Customer:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def showCustomer(self):
        print("{}, {}, {}".format(self.name, self.phone, self.email))

    def toCSV(self):
        return "{},{},{}\n".format(self.name, self.phone, self.email)


# a means -> append mode
file = open("customers.csv", "a")

print("==Welcome to Customer Management Solution==")
print(">> Enter 1 to Add a New Customer")

choice = int(input("Enter Your Choice: "))

if choice == 1:
    cRef1 = Customer(None, None, None)

    cRef1.name = input("Enter Customer Name: ")
    cRef1.phone = input("Enter Customer Phone: ")
    cRef1.email = input("Enter Customer Email: ")

    cRef1.showCustomer()

    saveChoice = input(">> Would you like to save {} ? (yes/no)".format(cRef1.name))
    if saveChoice == "yes":
        file.write(cRef1.toCSV())
        file.close()
        print(">> Customer Saved !!")
