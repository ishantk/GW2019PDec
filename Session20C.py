class CA:
    print(">> Hello !! This is Awesome")
    print(">> Wow !! This is more Awesome")

    def __init__(self):
        print(">> This is Constructor")

class CB(CA):
    print(">> Hello !!")
    print(">> Wow !!")


cRef1 = CA()
cRef2 = CA()


