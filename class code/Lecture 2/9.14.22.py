from functools import reduce

def dbl(x):
    return 2*x

def add(x,y):
    return x+y

def square1(x,y):
    return x+y**2

def square2(x):
    return x*x

def span(l):
    mx = reduce(max,l)
    mn = reduce(min, l)
    return mx - mn

def gauss(N):
    return reduce(add, range(N+1))
    #range(N+1) starts counting at 1 and goes until the last counting number of N
    # if N is 5, range(N+1) gives 1, 2, 3, 4, 5 (5 is included because + 1)

def sumOfSquares(N):
    return reduce(square1, range(N+1))

def sumOfSquares2(N):
    l = list(map(square2, range(N+1)))
    return(reduce(add, l))

print("Gauss of 5: ", gauss(5))
print("sumOfSquares1 of 5: ", sumOfSquares(5))
print("sumOfSquares2 of 5: ", sumOfSquares2(5))

print(reduce(add, [1,2,3,4]))

print("max-min 1: ", span([3,1,42,7]))
print("max-min 2: ", span([42,42,42,42]))


