# def employee(eid, name, salary):


# kwargs -> Key Word Arguments
def employee(**kwargs):
    print(kwargs)
    print(type(kwargs))


employee(eid=101, name="John", salary=30000)
employee(eid=201, name="Fionna", salary=40000, address="Redwood Shores")


def divide(num1, num2):
    result = num1 // num2
    print(">> Result:", result)


divide(10, 3)
divide(3, 10)

divide(num1=10, num2=3)
divide(num2=3, num1=10)

