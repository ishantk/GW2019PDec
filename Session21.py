# Whatever we write in class belongs to class
# what goes into object is just data represented by self i.e. attribute created in constructor
# other functions are meant to process the data
class Counter:

    # Property of class, it will not be an attribute of object
    # attribute of class
    myCount = 0

    def __init__(self):
        self.count = 1
        Counter.myCount = 1

    def incrementCount(self):
        self.count = self.count + 1
        Counter.myCount = Counter.myCount + 1

    def decrementCount(self):
        self.count = self.count - 1
        Counter.myCount = Counter.myCount - 1

    def showCount(self):
        print("Count is: {} and myCount is: {}".format(self.count, Counter.myCount))


c1 = Counter()      # count : 1   myCount : 1
c2 = Counter()      # count : 1   myCount : 1
c3 = c1

# c1 and c3 points to the same object
print(c1)
print(c2)
print(c3)

print(c1.__dict__)
print(c2.__dict__)
print(Counter.__dict__)

# Counter.incrementCount(c1)
c1.incrementCount()  # count : 2  myCount : 2
c2.incrementCount()  # count : 2  myCount : 3
c2.incrementCount()  # count : 3  myCount : 4

c1.decrementCount()  # count : 1 myCount : 3
c1.decrementCount()  # count : 0 myCount : 2
c1.decrementCount()  # count : -1 myCount : 1

c3.decrementCount()  # count : -2 myCount : 0
c3.incrementCount()  # count : -1 myCount : 1
c1.decrementCount()  # count : -2 myCount : 0

c4 = Counter()       # count : 1  myCount : 1
c4.incrementCount()

c1.showCount()     # Count is: -2 and myCount is: 1 2
c2.showCount()     # Count is:  3 and myCount is: 1 2
c3.showCount()     # Count is: -2 and myCount is: 1 2
c4.showCount()     # Count is:  2 and myCount is: 1 2



