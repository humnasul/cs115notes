def f():
    L = [1,2,3,4]
    M = g(L)
    print(L)
    print(M)

def g(List):
    return list(map, lambda x:x+1, List))

f()
# id() can be used to see if two elements have the same reference
