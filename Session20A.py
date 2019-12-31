class Parent:

    def __init__(self, fname, lname, wealth, car):
        self.fname = fname
        self.lname = lname
        self.wealth = wealth
        self.car = car

    def show(self):
        print(">> Name: {} {}".format(self.fname, self.lname))
        print(">> Wealth: {}".format(self.wealth))
        print(">> Car: {}".format(self.car))


# Child(Parent) -> Inheritance i.e. relationship established
class Child(Parent):
    pass


p1 = Parent("John", "Watson", 100000, "Honda City")
p1.show()

c1 = Child("Fionna", "Watson", 200000, "Honda Brio")
c1.show()

# Let us print what is in Parent Class
print(">> Parent Class Dictionary")
print(Parent.__dict__)

print(">> Child Class Dictionary")
print(Child.__dict__)

# Rule#1 : If child wish, it can access property of Parent in case it does not have it

