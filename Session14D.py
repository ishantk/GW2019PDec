def fun(*args, **kwargs):
    print(args)
    print(kwargs)


# execute the program by passing inputs
# fun(......)
fun(2, 3)
fun(2, 3, a=10, b=20)
# fun(2, 3, a=10, b=20, 10, 20)
# fun(num1=2, num2=3, a=10, b=20)

