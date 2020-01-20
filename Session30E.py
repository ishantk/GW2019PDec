# import datetime
import datetime as dt

# today = datetime.datetime.today()

today = dt.datetime.today()
print(">> Today:", today)

tomorrow = dt.datetime(2020, 1, 21, 16, 33, 10)
print(">> Tomorrow:", tomorrow)

howManyDays = tomorrow - today
print(">> howManyDays:", howManyDays)

# HW: Formatting of DateTime

