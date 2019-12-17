def buyBasketball(size):

    if size == 5:
        price = 18
    elif size == 6:
        price = 20
    elif size == 7:
        price = 24
    else:
        price = 0

    price = price + 50
    return price

size = int(input("Enter BasketBall Size you Wish to Buy: "))
priceToPay = buyBasketball(size)

if priceToPay > 50:
    print(">> You Need to Pay:", buyBasketball(size))
else:
    print(">> Size Not Available")

