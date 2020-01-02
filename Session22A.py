# Import All with Module Name Access
import Session22

print(">> This is Module: Session22A")

# PS: __name__ is name of module. but if you execute the module __name__ becomes __main__
print(">> Session22A __name__ is:", __name__)

# Unable to access created num of Session22 in Session22A
# print(">> num is:",num)  # error

# solution
# access content of Session22 by its name
print(">> num is:", Session22.num)   # OK | Belongs to Session22

# Same container created in Session22A
num = 100
print(">> num is:", num)             # OK | Belongs to Session22A

Session22.show()

cRef = Session22.CA()
cRef.hello()

