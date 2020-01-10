from tkinter import *
from Session25 import Customer
from Session26 import DBHelper

def onClick():

    customer = Customer(None, None, None)
    customer.name = entryName.get()
    customer.phone = entryPhone.get()
    customer.email = entryEmail.get()

    customer.showCustomer()

    db = DBHelper()
    db.saveCustomer(customer)


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

