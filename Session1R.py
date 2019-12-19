# Model : Data Storage

# Single Value Containers
# They can store only and only 1 single value

# Storage Creation Statements
sourceLocation = "Model Town"
destinationLocation = "MBD Mall"
typeOfCab = "UberGo"
fare = 120.22

# Computation Statements
taxes = 0.1 * fare
totalFare = fare + taxes

# Read Statements
print(sourceLocation)
print(destinationLocation)
print(typeOfCab)
print(fare)
print(taxes)
print("Total Fare to be Paid is:", totalFare)

# Update Statements
totalFare = totalFare + 10
print("Total Fare to be Paid with a hike fee is:", totalFare)
