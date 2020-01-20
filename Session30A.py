# User Defined Exception or Error
class BankingError(Exception):
    pass

class BankAccount:

    def __init__(self):
        self.balance = 10000
        self.attempts = 0

    def withdraw(self, amount):
        self.balance = self.balance - amount
        if self.balance > 0:
            print(">> New Balance is: \u20b9", self.balance)
        else:
            self.balance = self.balance + amount
            print(">> Sorry !! Balance is LOW \u20b9", self.balance)
            self.attempts += 1

        if self.attempts == 3:
            # error = IndexError("Illegal Attempts !!")
            error = BankingError("Illegal Attempts !!")
            raise error  # We are going to crash our program :)


print(">> Banking Started")
johnsAccount = BankAccount()

for _ in range(0, 500):
    johnsAccount.withdraw(3000)

print(">> Banking Finished")