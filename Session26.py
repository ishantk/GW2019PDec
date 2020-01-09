import mysql.connector as ms

class DBHelper:

    def __init__(self):
        self.con = ms.connect(user="root", password="", host="127.0.0.1", database="auridb")

    def saveCustomer(self, customer):
        sql = "insert into Customer values(null, '{}', '{}', '{}')".format(customer.name, customer.phone, customer.email)
        cursor = self.con.cursor()
        cursor.execute(sql)
        self.con.commit()
        print(">> CUSTOMER SAVED")

    def updateCustomer(self, customer):
        sql = "update Customer set name = '{}', phone = '{}', email='{}' where cid = {}".format(customer.name, customer.phone, customer.email, customer.cid)
        cursor = self.con.cursor()
        cursor.execute(sql)
        self.con.commit()
        print(">> CUSTOMER UPDATED")

    def deleteCustomer(self, cid):
        sql = "delete from Customer where cid = {}".format(cid)
        cursor = self.con.cursor()
        cursor.execute(sql)
        self.con.commit()
        print(">> CUSTOMER DELETED")

    def getAllCustomers(self):
        sql = "select * from Customer"
        cursor = self.con.cursor()
        cursor.execute(sql)

        rows = cursor.fetchall()

        for row in rows:
            # print(row)
            print("{} | {}".format(row[0], row[1]))

    def getCustomerByCID(self, cid):
        sql = "select * from Customer where cid = {}".format(cid)
        cursor = self.con.cursor()
        cursor.execute(sql)

        row = cursor.fetchone()

        if row is not None:
            print(row)
            # print("{} | {}".format(row[0], row[1]))
        else:
            print(">> NO CUSTOMER FOUND at CID {}".format(cid))

