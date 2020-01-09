"""

    DataBase : Store Data
    1. SQL
        We store data in the form of tables
        Offline / Online(Centralized)
        MySQL and Oracle
    2. NoSQL
        We store data in the form of documents
        Online/Cloud

    create table Customer(
        cid int primary key auto_increment,
        name varchar(256),
        phone varchar(20),
        email varchar(256)
    )

    insert into Customer values(null, 'John', '+91 99999 88888', 'john@example.com')
    update Customer set name = 'kia watson', phone = '+91 90000 98765', email='kia.watson@example.com' where cid = 3
    delete from Customer where cid = 1
    select * from Customer

    For Detailed Study on SQL : https://www.w3schools.com/sql/

    Python MySQL Connection
    1. Add mysql-connector library to your project
    2. import mysql.connector as anyname of your choice
    3. create connection |user, pass, host, db
    4. write sql statement and substitute data in it
    5. obtain cursor which is responsible to perform db operation i.e. execute sql statements
    6. commit the statement



"""

# import mysql.connector as ms
from Session26 import DBHelper

class Customer:

    def __init__(self, name, phone, email):
        self.cid = 0
        self.name = name
        self.phone = phone
        self.email = email

    def showCustomer(self):
        print("{}, {}, {}".format(self.name, self.phone, self.email))

    def toCSV(self):
        return "{},{},{}\n".format(self.name, self.phone, self.email)


# a means -> append mode
# file = open("customers.csv", "a")

# Creating a Connection with DataBase
# localhost -> 127.0.0.1
# con = ms.connect(user="root", password="", host="127.0.0.1", database="auridb")

print("==Welcome to Customer Management Solution==")
print(">> Enter 1 to Add a New Customer")
print(">> Enter 2 to Update Existing Customer")
print(">> Enter 3 to Delete Existing Customer")
print(">> Enter 4 to Get All Existing Customers")
print(">> Enter 5 to Find Customer by ID")

choice = int(input("Enter Your Choice: "))

if choice == 1:
    customer = Customer(None, None, None)

    customer.name = input("Enter Customer Name: ")
    customer.phone = input("Enter Customer Phone: ")
    customer.email = input("Enter Customer Email: ")

    customer.showCustomer()

    # saveChoice = input(">> Would you like to save {} ? (yes/no)".format(cRef1.name))
    # if saveChoice == "yes":
    #     # file.write(cRef1.toCSV())
    #     # file.close()
    #
    #     sql = "insert into Customer values(null, '{}', '{}', '{}')".format(cRef1.name, cRef1.phone, cRef1.email)
    #     cursor = con.cursor()
    #     cursor.execute(sql)
    #     con.commit()
    #
    #
    #     print(">> Customer Saved !!")

    saveChoice = input(">> Would you like to save {} ? (yes/no)".format(customer.name))

    if saveChoice == "yes":
        db = DBHelper()
        db.saveCustomer(customer)

elif choice == 2:

    customer = Customer(None, None, None)
    customer.cid = int(input("Enter Customer ID: "))


    customer.name = input("Enter Customer Name: ")
    customer.phone = input("Enter Customer Phone: ")
    customer.email = input("Enter Customer Email: ")

    customer.showCustomer()

    updateChoice = input(">> Would you like to Update {} ? (yes/no)".format(customer.name))

    if updateChoice == "yes":
        db = DBHelper()
        db.updateCustomer(customer)

elif choice == 3:
    cid = int(input("Enter Customer ID: "))

    deleteChoice = input(">> Would you like to Delete {} ? (yes/no)".format(cid))

    if deleteChoice == "yes":
        db = DBHelper()
        db.deleteCustomer(cid)

elif choice == 4:
    db = DBHelper()
    db.getAllCustomers()

elif choice == 5:
    cid = int(input("Enter Customer ID: "))
    db = DBHelper()
    db.getCustomerByCID(cid)