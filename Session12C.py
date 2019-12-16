students = ["John", "Jennie", "Jack"]
rollNums = [1, 2, 3]
courses = ['Python', 'Java', 'C++']

for i in range(0, len(students)):
    print("{} has roll number {} and is enrolled for {}"
          .format(students[i], rollNums[i], courses[i]))

# Challenge : To store lot of data we need to maintain different lists
# Solution  : Dictionary -> Key Value Pair
student1 = {"name": "John", "rollNum": 1, "course": "Python"}
student2 = {"name": "Jennie", "rollNum": 2, "course": "Java"}
student3 = {"name": "Jack", "rollNum": 3, "course": "C++"}

print(student1)
print(student2)
print(student3)

student1["name"] = "John Watson"
student2["rollNum"] = 22
student3["course"] = "C/C++"

print(student1)
print(student2)
print(student3)

print("{} has roll number {} and is enrolled for {}"
      .format(student1["name"], student1["rollNum"], student1["course"]))

keys = list(student1.keys())

print()

for key in keys:
    # print(key)
    print(key, "|", student1[key])
    print(key, "|", student2[key])
    print(key, "|", student3[key])


    