# Loops/Iterations
# while and for

# List
# Indexing  0     1     2    3    4     5
products = [100, 123, 345, 124, 6765, 134]

# Use Case : On All the Product Prices a flat 20% has to be calculated

"""
discountedPrice = products[0] - (0.2 * products[0])
print(">> discountedPrice: ",discountedPrice)

discountedPrice = products[1] - (0.2 * products[1])
print(">> discountedPrice: ",discountedPrice)

discountedPrice = products[2] - (0.2 * products[2])
print(">> discountedPrice: ",discountedPrice)

discountedPrice = products[3] - (0.2 * products[3])
print(">> discountedPrice: ",discountedPrice)

discountedPrice = products[4] - (0.2 * products[4])
print(">> discountedPrice: ",discountedPrice)

discountedPrice = products[5] - (0.2 * products[5])
print(">> discountedPrice: ",discountedPrice)
"""

# While Loop
idx = 0
while idx < 6:
    discountedPrice = products[idx] - (0.2 * products[idx])
    print(">> discountedPrice: ", discountedPrice)
    # idx = idx + 1
    idx += 1

print("=======")

# Simple/Basic For Loop
for i in range(0, 6):
    discountedPrice = products[i] - (0.2 * products[i])
    print(">> discountedPrice: ", discountedPrice)

print("=======")

# For-Each Loop / Enhanced For Loop
for price in products:
    discountedPrice = price - (0.2 * price)
    print(">> discountedPrice: ", discountedPrice)

