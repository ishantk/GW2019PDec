class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # self here, points to object
    def showPoint(self):
        print("Point is: {} : {}".format(self.x, self.y))

    # cls here, points to object
    # def createPoint(cls, data):

    @classmethod                # After decorating the method : cls here, points to class
    def createPoint(cls, data):
        points = data.split(",")
        refToObject = cls(int(points[0]), int(points[1]))  # execute init
        return refToObject

p1 = Point(10, 20)
p1.showPoint()


p2 = Point.createPoint("30,40")
p2.showPoint()


