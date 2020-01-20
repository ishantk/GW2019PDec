print(">> App Started")

numbers = [10, 20, 30, 40, 50]
a = 10
b = 0
c = 0
idx = int(input(">> Enter an Index: "))
"""
try:
    print(">> number at idx {} is: {}".format(idx, numbers[idx]))
    c = a // b
    # print(">> This must be executed")
except IndexError as iRef:
    print(">> Some Error:", iRef)
except ZeroDivisionError as zRef:
    print(">> Some Error:", zRef)
finally:
    print(">> This must be executed")
"""

try:
    print(">> number at idx {} is: {}".format(idx, numbers[idx]))
    c = a // b
    # print(">> This must be executed")
except Exception as e:
    print(">> Some Error:", e)
finally:
    print(">> This must be executed")


print(">> c is:", c)

print(">> App Finished")
# PS: Whenever error will occur in python program
#     it will be always RUN TIME ERROR
#     Whenever Run time error will occur, Program will CRASH
"""
    Regular try except finally
    try:
        pass
    except:
        pass
    finally:
        pass
        
     
    Nested try except finally    
    try:
        try:
            pass
        except:
            pass
        finally:
            pass
    except:
        try:
            pass
        except:
            pass
        finally:
            pass
    finally:
        try:
            pass
        except:
            pass
        finally:
            pass
"""

