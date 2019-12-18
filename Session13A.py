def buyBasketball(size, shipping=50):

    if size == 5:
        price = 18
    elif size == 6:
        price = 20
    elif size == 7:
        price = 24
    else:
        price = 0

    price = price + shipping
    return price

size = int(input("Enter BasketBall Size you Wish to Buy: "))
# priceToPay = buyBasketball(size)
shipping = 70
priceToPay = buyBasketball(size, shipping)

if priceToPay > shipping:
    print(">> You Need to Pay:", buyBasketball(size, shipping))
else:
    print(">> Size Not Available")

