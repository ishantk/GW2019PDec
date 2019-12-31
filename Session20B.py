class Parent:
    def __init__(self):
        print(">> Parent Constructor")

    def show(self):
        print(">> This is Parent's Show")


class Child(Parent):
    def __init__(self):
        Parent.__init__(self)  # Accessing Parent's Features
        print(">> Child Constructor")

    def show(self):
        Parent.show(self)
        print(">> This is Child's Show")


c1 = Child()
c1.show()

print(Parent.__dict__)
print(Child.__dict__)


# Rule #2 : If Parent has properties, and child also creates its own properties,
#           then, child will access its own properties and not of Parents

# Rule #3 : If Parent has properties, and child also creates its own properties,
#           then, child will access its own properties and not of Parents
#           If Child, wish to access parent's properties, we need to user Parent class name to access
