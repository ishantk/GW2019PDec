# Conditional Flow
# if/else | Nested if/else | Ladder if/else

# Use Case : apply promo code
#            flat 50% off of amount is > 500
#            otherwise no discounts

amount = float(input("Enter Your Final Billing Amount: "))
print(">> You Entered:", amount)

# Basic/Regular/Simple -> if/else

"""
if amount > 500:
    discount = 0.5 * amount
    amountToPay = amount - discount
    print(">> You Get a Flat 50% Discount of \u20b9", discount, "Please Pay \u20b9",amountToPay)
else:
    print(">> Sorry !! No Discounts on \u20b9", amount)
"""


# Use Case : apply promo code
#            Slab1 : Flat 30% for 200 to 500
#            Slab2 : Flat 20% for 100 to 200
#            flat 50% off of amount is > 500
#            otherwise no discounts

# Ladder if/else

if amount >=100 and amount <200:
    discount = 0.2 * amount
    amountToPay = amount - discount
    print(">> You Get a Flat 20% Discount of \u20b9", discount, "Please Pay \u20b9", amountToPay)
elif amount >=200 and amount <500:
    discount = 0.3 * amount
    amountToPay = amount - discount
    print(">> You Get a Flat 30% Discount of \u20b9", discount, "Please Pay \u20b9", amountToPay)
elif amount >= 500:
    discount = 0.5 * amount
    amountToPay = amount - discount
    print(">> You Get a Flat 50% Discount of \u20b9", discount, "Please Pay \u20b9", amountToPay)
else:
    print(">> Sorry !! No Discounts on \u20b9", amount)

# Explore to show only upto 2 decimal values

# Nested if/else
isInternetOn = True
isGPSOn = False

if isInternetOn:
    print(">> Allow User to Access Google Maps")
    if isGPSOn:
        print(">> Allow User to Navigate with Google Maps")
    else:
        print(">> Please Enable GPS and Try Again !!")
else:
    print(">> Please Enable Internet and Try Again !!")




