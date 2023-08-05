def dbl(x):
    return 2*x
formula = dbl(5) // 2
print(formula)

print(list(map(dbl, [0,1,2,3,4])))

def evens(n):
        return list(map(dbl, range(n))))
