S1 = {1, 2, 3, 'a', 'b'}
S2 = {1, 'a', 'b'}

print(1 in S1)
print('b' in S2)

print(S2.issubset(S1))
print(S1.issuperset(S2))

S1.union(S2) # MUTABLE
print(S1)

S1.intersection(S2)
S1.difference(S2)
# S1.symmetric_difference(S2)   # Please Explore symmetric_difference

