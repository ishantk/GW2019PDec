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


    Python MySQL Connection
    1. Add mysql-connector library to your project
    2. import mysql.connector as anyname of your choice
    3. create connection |user, pass, host, db
    4. write sql statement and substitute data in it
    5. obtain cursor which is responsible to perform db operation i.e. execute sql statements
    6. commit the statement



"""

import mysql.connector as ms

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
# file = open("customers.csv", "a")

# Creating a Connection with DataBase
# localhost -> 127.0.0.1
con = ms.connect(user="root", password="", host="127.0.0.1", database="auridb")

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
        # file.write(cRef1.toCSV())
        # file.close()

        sql = "insert into Customer values(null, '{}', '{}', '{}')".format(cRef1.name, cRef1.phone, cRef1.email)
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()


        print(">> Customer Saved !!")

