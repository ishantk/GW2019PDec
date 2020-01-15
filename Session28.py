from Session25 import Customer
from tkinter import *
import firebase_admin
from firebase_admin import credentials

from firebase_admin import firestore

cred = credentials.Certificate("ServiceAccountKey.json")
firebase_admin.initialize_app(cred)

# Insert Data in FirebaseFirestore
"""
customer = Customer("John", "+91 99999 66666", "john@example.com")
customer.cid = 1
# print(customer)
# print(customer.__dict__)

# Here we are getting data of Object as dictionary
customerData = customer.__dict__
# print(customerData, type(customerData))

# in Firebase if we need to save data it should be as dictionary
db = firestore.client()
db.collection("customers").document(customer.phone).set(customerData)
print(">> Customer Saved in FirebaseFirestore")
"""


from Session25 import Customer

def onClick():

    customer = Customer(None, None, None)
    customer.name = entryName.get()
    customer.phone = entryPhone.get()
    customer.email = entryEmail.get()
    customer.cid = 2

    customer.showCustomer()
    customerData = customer.__dict__
    db = firestore.client()
    db.collection("customers").document(customer.email).set(customerData)
    print(">> Customer Saved in FirebaseFirestore")


# Create a GUI Window
window = Tk()
# print(type(window)) -> class tkinter.Tk

lblTitle = Label(window, text="Customer Management System")
lblTitle.pack()     # To add the label in window

lblName = Label(window, text="Enter Customer's Name")
lblName.pack()

entryName = Entry(window)
entryName.pack()

lblPhone = Label(window, text="Enter Customer's Phone")
lblPhone.pack()

entryPhone = Entry(window)
entryPhone.pack()

lblEmail = Label(window, text="Enter Customer's Email")
lblEmail.pack()

entryEmail = Entry(window)
entryEmail.pack()

btnAddCustomer = Button(window, text="Add Customer", command=onClick)
btnAddCustomer.pack()

# Show the GUI Window in an infinite loop
window.mainloop()

