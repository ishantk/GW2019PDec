def squareofNumber(num=2):
    return num * num

lRef = lambda num=2: num * num

numbers = [10, 20, 30, 40, 50]

# result = map(squareofNumber, numbers)
result = map(lRef, numbers)
print(result)
print(list(result))


numbers = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
lm1 = lambda n: n % 2 == 0
lm2 = lambda n: n % 2 != 0

result = map(lm1, numbers)
print(list(result))


result = filter(lm1, numbers)
print(list(result))
result = filter(lm2, numbers)
print(list(result))

employees = [
                {"eid": 1, "name": "John", "salary": 30000, "email": "john@example.com"},
                {"eid": 2, "name": "Jennie", "salary": 40000, "email": "jennie@example.com"},
                {"eid": 3, "name": "Jim", "salary": 50000, "email": "jim@example.com"}
            ]

lm3 = lambda emps: emps["name"]
result = map(lm3, employees)
print(list(result))

punjabPopulation = [12341, 2123, 4321, 4541, 8908]
totalPopulation = 0
for population in punjabPopulation:
    totalPopulation = totalPopulation + population

print(">> totalPopulation:", totalPopulation)

from functools import reduce
lm4 = lambda x, y: x+y
result = reduce(lm4, punjabPopulation)
print(result)


# HW: Create 2 lists of same size with integer numbers
#     Create 2 lists of different size with integer numbers
#     Use lm4 and write map function to see if 2 lists are added to get a new list or not



