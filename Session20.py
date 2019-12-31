"""
    eCommerce Platform

    OOPS:
    1. Think of an Object
    MobilePhone : pid, name, brand, price, color, ram, storage, os
    LEDTv       : pid, name, brand, price, color, size, technology
    Shoe        : pid, name, brand, price, color, shoeSize

    Chellenge:
        For n-number of products we will have common attributes
        It means we will have to write same code again and again

    Solution:
        Inheritance | Parent Child Relationship
        If child does not have a certain attribute, it can access if prent has it in parent


"""

"""
class MobilePhone:

    def __init__(self, pid, name, brand, price, color, ram, storage, os):
        self.pid = pid
        self.name = name
        self.brand = brand
        self.price = price
        self.color = color
        self.ram = ram
        self.storage = storage
        self.os = os

    def showMobilePhone(self):
        print("======Mobile Phone=====")
        print("PID\t",self.pid)
        print("Name\t", self.name)
        print("Brand\t", self.brand)
        print("Price\t", self.price)
        print("Color\t", self.color)
        print("RAM\t", self.ram)
        print("Storage\t", self.storage)
        print("OS\t", self.os)
        print("=======================")


class LEDTv:

    def __init__(self, pid, name, brand, price, color, size, technology):
        self.pid = pid
        self.name = name
        self.brand = brand
        self.price = price
        self.color = color
        self.size = size
        self.technology = technology

    def showLedTv(self):
        print("======LED TV Details=====")
        print("PID\t",self.pid)
        print("Name\t", self.name)
        print("Brand\t", self.brand)
        print("Price\t", self.price)
        print("Color\t", self.color)
        print("Size\t", self.size)
        print("Technology\t", self.technology)
        print("=======================")


class Shoe:

    def __init__(self, pid, name, brand, price, color, shoeSize):
        self.pid = pid
        self.name = name
        self.brand = brand
        self.price = price
        self.color = color
        self.shoeSize = shoeSize

    def showShoe(self):
        print("======Shoe Details=====")
        print("PID\t",self.pid)
        print("Name\t", self.name)
        print("Brand\t", self.brand)
        print("Price\t", self.price)
        print("Color\t", self.color)
        print("Shoe Size\t", self.shoeSize)
        print("=======================")


m1 = MobilePhone(101, "iPhoneX", "Apple", 70000, "black", 3, 128, "ios")
l1 = LEDTv(201, "S-OLED", "Samsung", 50000, "silver", 50, "OLED")
s1 = Shoe(301, "AlphaBounce", "Adidas", 8000, "green", 8)

m1.showMobilePhone()

l1.showLedTv()

s1.showShoe()
"""

class Product:

    def __init__(self, pid, name, brand, price, color):
        self.pid = pid
        self.name = name
        self.brand = brand
        self.price = price
        self.color = color


    def showProduct(self):
        print("======Product Details=====")
        print("PID\t",self.pid)
        print("Name\t", self.name)
        print("Brand\t", self.brand)
        print("Price\t", self.price)
        print("Color\t", self.color)
        print("=======================")


# MobilePhone IS-A Product
class MobilePhone(Product):

    def __init__(self, pid, name, brand, price, color, ram, storage, os):
        Product.__init__(self, pid, name, brand, price, color)
        self.ram = ram
        self.storage = storage
        self.os = os

    def showMobilePhone(self):
        Product.showProduct(self)
        print("======Mobile Phone=====")
        print("RAM\t", self.ram)
        print("Storage\t", self.storage)
        print("OS\t", self.os)
        print("=======================")

# LEDTv IS-A Product
class LEDTv(Product):

    def __init__(self, pid, name, brand, price, color, size, technology):
        Product.__init__(self, pid, name, brand, price, color)
        self.size = size
        self.technology = technology

    def showLedTv(self):
        Product.showProduct(self)
        print("======LED TV Details=====")
        print("Size\t", self.size)
        print("Technology\t", self.technology)
        print("=======================")


# Shoe IS-A Product
class Shoe(Product):

    def __init__(self, pid, name, brand, price, color, shoeSize):
        Product.__init__(self, pid, name, brand, price, color)
        self.shoeSize = shoeSize

    def showShoe(self):
        Product.showProduct(self)
        print("======Shoe Details=====")
        print("Shoe Size\t", self.shoeSize)
        print("=======================")


m1 = MobilePhone(101, "iPhoneX", "Apple", 70000, "black", 3, 128, "ios")
l1 = LEDTv(201, "S-OLED", "Samsung", 50000, "silver", 50, "OLED")
s1 = Shoe(301, "AlphaBounce", "Adidas", 8000, "green", 8)

m1.showMobilePhone()

l1.showLedTv()

s1.showShoe()


# Implement PayTm Travel with Is-A Relationship
# Covering all the 5 types below explained
# and Share the Image


"""


    Inheritance Types
    
    1. Single Level
    
    CA
    |
    CB
    
    class CA:
        pass
    
    class CB(CA):
        pass
        
    2. Multi Level
    CA
    |
    CB
    |
    CC 
    
    class CA:
        pass
    
    class CB(CA):
        pass 
        
    class CC(CB):
        pass   
        
    3. Hierarchy
    
     CA
     |
  CB   CC  
    
    class CA:
        pass    

    class CB(CA):
        pass
        
    class CC(CA):
        pass 
        
   4. Multiple
   CA    CB
       |
       
       CC
       
    class CA:
        pass    

    class CB:
        pass
        
    class CC(CA, CB):
        pass 
        
   5. Hybrid
    Fuion of above         
           

"""