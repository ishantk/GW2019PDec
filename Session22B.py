# Import All with Module Alias Access
import Session22 as S2  # S2 is alias of Session22, which can be any name of your choice

print(">> This is Module: Session22B")

# PS: __name__ is name of module. but if you execute the module __name__ becomes __main__
print(">> Session22B __name__ is:", __name__)

# Unable to access created num of Session22 in Session22A
# print(">> num is:",num)  # error

# solution
# access content of Session22 by its name
print(">> num is:", S2.num)   # OK | Belongs to Session22

# Another container with same name created in Session22A also
num = 100
print(">> num is:", num)             # OK | Belongs to Session22A

S2.show()

cRef = S2.CA()
cRef.hello()

