
def applyPromoCode(promoCode, amount):

    if amount >= 100 and amount < 200:
        if promoCode == 1:
            amountToPay = amount - 0.2 * amount
            print(">> Discount of 20% applied: \u20b9", amountToPay)
        else:
            print(">> Please Use PromoCode 1 to get 20% Off")

    elif amount >= 200 and amount < 500:
        if promoCode == 2:
            amountToPay = amount - 0.3 * amount
            print(">> Discount of 30% applied: \u20b9", amountToPay)
        else:
            print(">> Please Use PromoCode 2 to get 30% Off")

    elif amount >= 500:
        if promoCode == 3:
            amountToPay = amount - 0.5 * amount
            print(">> Discount of 50% applied: \u20b9", amountToPay)
        else:
            print(">> Please Use PromoCode 3 to get 50% Off")

    else:
        print(">> Sorry No Discounts for \u20b9", amount)



"""
amount = int(input(">> Enter Amount"))
promoCode = int(input(">> Enter Promo Code"))

applyPromoCode(promoCode, amount)

amount = int(input(">> Enter Amount"))
promoCode = int(input(">> Enter Promo Code"))

applyPromoCode(promoCode, amount)
"""

choice = "yes"

while choice == "yes":
    amount = int(input(">> Enter Amount"))
    promoCode = int(input(">> Enter Promo Code"))

    applyPromoCode(promoCode, amount)

    choice = input("Would you like to apply promo code again? (yes/no)")