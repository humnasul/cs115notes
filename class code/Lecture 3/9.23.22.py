def mystery(item, L):
    NewL = map(lambda X : X == item, L)
    #if you use filter instead of map, it will only keep the true values in the list anyway
    print(list(NewL))
    return sum(NewL) > 0

def prime(n):
    possibleDivisors = range(2, n)
    divisors = filter(lambda x: n % x == 0, possibleDivisors)
    return len(list(divisors)) == 0

def sieve(L):
    if L == []: return []
    else:
        return list(filter(lambda x : x % L[0] != 0, L[1:]))

mystery(12, [1,3,5,12,300])
print(sieve(range(1, 101)))
