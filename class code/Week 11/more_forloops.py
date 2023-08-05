for i in range(10):
    print(i)
for symbol in "CS115":
    print(symbol)

#names = {"Liz"}

for i in range(1, 66, 2):
    print(i)
for i in range(1, 66):
    if i % 2 == 1:
        print(i)
x = 1
while x < 67:
    print(x)
    x+=2

[print(n) for n in range(1,66,2)]

def mapSqr(L):
    for x in range(len(L)):
        L[x] = L[x] * L[x]
    return L

def mapSqr2(L):
    return [i**2 for i in L]

print(mapSqr([1, 2, 3]))
print(mapSqr2([1, 2, 3]))
