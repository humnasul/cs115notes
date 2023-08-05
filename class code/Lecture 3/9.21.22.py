def length(lst):
    if lst == []:
        return 0
    else:
        return 1 + len(lst[1:])
def divides(n):
    def div(k):
            return n % k == 0
    return div

'''def dbl(x):
    return 2*x'''

dbl = lambda x : x*2

print(dbl(10))

'''
f = divides(15)
print(f(3))
f = divides(10)
print(f(4))

print(length([1,2,[3,4]]))
'''

print(list(filter(lambda x: x % 2 == 0, range(100))))
print(list(filter(lambda lst: len(lst) <= 2, [["spam", "yum"], [42], [1,23]])))
print(list(map(lambda squares : squares**2, range(10,51))))
