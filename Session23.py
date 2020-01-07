"""
    A Quick Approach to Solve KnapSack :)

    2
    0 0
    0 1
    1 0
    1 1

"""

capacity = 20
weights = [20, 10, 9, 4, 2, 1]
value = [4000, 3500, 1800, 400, 1000, 200]

def generateCombinations(num):

    combinations = []

    for i in range(0, 2**num):
        combination = []

        for j in range(num-1, -1, -1):
            combination.append(i // 2**j % 2)

        # combination.append(i // 32 % 2)
        # combination.append(i // 16 % 2)
        # combination.append(i // 8 % 2)
        # combination.append(i // 4 % 2)
        # combination.append(i // 2 % 2)
        # combination.append(i % 2)

        # combination = "{} {} {} {}".format(i//8%2, i//4%2, i//2%2, i%2)

        combinations.append(combination)

    # combinations is a list of lists
    return combinations


combinations = generateCombinations(len(weights))


for comb in combinations:
    print(comb)


results = []
weightResults = []
valueResults = []


for comb in combinations:

    totalWeight = 0
    totalValue = 0
    
    for i in range(0, len(comb)):
        if comb[i] == 1:
            totalWeight = totalWeight + weights[i]
            totalValue = totalValue + value[i]

    if totalWeight <= capacity:
        results.append("{} - {}".format(totalWeight, totalValue))
        weightResults.append(totalWeight)
        valueResults.append(totalValue)


# for result in results:
#     print(result)

for i in range(0, len(weightResults)):
    print(weightResults[i], " | ", valueResults[i])