# Multiple Arguments : can be any number :)
# Variable Arguments / VarArgs
# Arguments or Inputs
def addNumbers(*args):
    # print(args)
    # print(type(args)) # tuple -> tuple is indexed from 0 to n-1
    # print(args[0])

    sum = 0
    for idx in range(0, len(args)):
        sum = sum + args[idx]

    # print(">> sum is:", sum)
    print(">> sum of all elements in", args, "is:", sum)


addNumbers(10)
addNumbers(11, 20)
addNumbers(12, 20, 30, 40, 50)
addNumbers(13, 20, 30, 40, 50, 60, 70, 80, 90, 100)
