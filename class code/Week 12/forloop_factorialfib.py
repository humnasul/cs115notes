def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= 1
    return fact

def fibonacci(n):
    L = [0,1]
    for i in range(2, n+1):
        L.append(L[i-1]+L[i-2])
    return L[n]

print(list(range(5,1,-1)))
print(fibonacci(5))
