class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def showPoint(self):
        print(">> Point is: {} : {}".format(self.x, self.y))


p1 = Point(10, 20)

# Execute Function with Object's Reference
# p1.showPoint()

# Execute Function with Class Name
# Pass Reference Variable in place of self
Point.showPoint(p1)
