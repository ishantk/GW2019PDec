S = {1, 2, 3, 'a','b'}
S.add('c')

print(S)

S.remove('a')
S.remove(1)

print(S)

# PS: Set stores data using Hashing technique and not indexing

S.clear()
print(S)

data = [10, 20, 30]
data.clear()

print(data)