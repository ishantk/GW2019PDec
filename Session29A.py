class Customer:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    @classmethod
    def readCustomersCSVFile(cls):

        cls.customers = []

        file = open("customers.csv", "r")
        lines = file.readlines()

        for line in lines:
            data = line.split(",")
            refToObject = cls(data[0], data[1], data[2]) # Execute Constructor
            cls.customers.append(refToObject)

    def showCustomer(self):
        print("Customer: {} | {} | {}".format(self.name, self.phone, self.email))

    @staticmethod
    def checkGreater(num1, num2): # In which we can eliminate self and cls
        return num1 > num2


Customer.readCustomersCSVFile()
print(Customer.customers)

for customer in Customer.customers:
    customer.showCustomer()

print("Is 10 > 20?", Customer.checkGreater(10, 20))