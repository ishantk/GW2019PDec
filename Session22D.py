# Import selective things
from Session22 import num
from Session22 import show

# from Session22 import CA


print(">> This is Module: Session22D")

# PS: __name__ is name of module. but if you execute the module __name__ becomes __main__
print(">> Session22D __name__ is:", __name__)

# solution
# access content of Session22 by its name
print(">> num is:", num)   # OK | Belongs to Session22

# Same container created in Session22
num = 100   # Update
print(">> num is:", num)             # OK | Belongs to Session22A

show()

# error : Because class CA is not imported
# cRef = CA()


