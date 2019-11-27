# Monday to Thursday | 1 hour content delivery | 1 hour -> practical

# This is Session1 - A Comment Statement

# Container Creation Statement
# usersOnMonday = 12000
# usersOnTuesday = 7500

usersOnMonday = int(input("Enter Users on Monday: "))
usersOnTuesday = int(input("Enter Users on Tuesday: "))
profits = 219.9

# Container Updation Statement
usersOnMonday = 11000

# Computational Statements
profitsOnMonday = usersOnMonday * profits
profitsOnTuesday = usersOnTuesday * profits

totalProfits = profitsOnMonday + profitsOnTuesday


# Read Statement
print("Users on Monday", usersOnMonday)
print("Users on Tuesday", usersOnTuesday)

print("Profits Made are", totalProfits)

# Logical Statements
# We wish to know profits were better on monday or tuesday
if profitsOnMonday > profitsOnTuesday:
    print("Monday had more profits", profitsOnMonday)
else:
    print("Tuesday had more profits")

