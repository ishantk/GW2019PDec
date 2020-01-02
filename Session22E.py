import pack1.One

print(">> This is Module: Session22E")

# PS: __name__ is name of module. but if you execute the module __name__ becomes __main__
print(">> Session22E __name__ is:", __name__)

print(">> num is:", pack1.One.num)

pack1.One.show()

cRef = pack1.One.CA()
cRef.hello()



