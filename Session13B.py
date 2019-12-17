# quotes = ["Love For All, Hatred For None. – Khalifatul Masih III",
#           "Change the world by being yourself. – Amy Poehler",
#           "Every moment is a fresh beginning. – T.SEliot"]
# print(quotes)
# print(len(quotes))
# print(quotes[0])
# print(quotes[1])
# print(quotes[2])

import random

def showQuote():
    quotes = ["Love For All, Hatred For None. – Khalifatul Masih III",
              "Change the world by being yourself. – Amy Poehler",
              "Every moment is a fresh beginning. – T.SEliot"]

    setOfNumbers = set(range(0,20))

    index = 0

    # quote = random.choice(quotes)

    return quotes[index]

print(">> ",showQuote())
print(">> ",showQuote())
print(">> ",showQuote())


otps = list(range(1000, 10000))
idx = 10

def sendOTP():
    global idx

    otp = otps[idx]

    idx = (idx * 3)//2      # enhance the logic of Random Number Generation

    return otp

print("OTP 1:",sendOTP())
print("OTP 2:",sendOTP())
print("OTP 3:",sendOTP())
print("OTP 4:",sendOTP())


