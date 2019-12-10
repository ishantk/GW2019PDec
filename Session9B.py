ipAddresses = ["198.19.11.1", "198.19.10.2", "198.11.10.3", "198.10.10.4", "198.20.10.5" ]
print(ipAddresses)

print()

# Update Data in List
ipAddresses[1] = "202.1.1.20"
print(ipAddresses)

print()

# Delete Data in List
del ipAddresses[2] # deletes index

print()

print(ipAddresses[2])
print(ipAddresses[-2])

# List can be Homo/Hetrogeneous
data = [1, "Jennie", 2, 3, "John", "Jennie", "Jim"]
print(">> data is:", data)
data.remove(3)      # removes Matching Data
data.remove("Jennie")
print(">> data after removing 3 is:", data)

data.pop(2) # deletes index
print(">> data after popping 2 is:", data)

