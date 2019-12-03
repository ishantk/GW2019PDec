for i in range(1, 6):           # 1 to 5
    # print(">> i is:", i)
    # print(i)
    for j in range(1, i + 1):
        # print(">> j is:", j)
        print(j, end=" ")

    print()

"""    
i : 0
j : 0

i : 1
j : 0 1

i : 2
j : 0 1 2

i : 3
j : 0 1 2 3

i : 4
j : 0 1 2 3 4

i : 5
j : 0 1 2 3 4 5

"""


# Assignment
# Patern
"""
1
1 1
1 1 1
1 1 1 1
1 1 1 1 1

1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15

Calculate Sum of Rows and Sum of Columns 
Rows > Columns or Columns > Rows or Rows == Columns
"""