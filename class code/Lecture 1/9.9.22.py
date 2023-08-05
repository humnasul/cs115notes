def dbl(x):
    result = 2*x
    return result

print(dbl(dbl(2)))

def myFunc(x,y):
        return x + 42 * y

print(myFunc(2,1))

def area(r):
    """
        Input: radius r
        Output: area of the circle
    """
    return 3.14*(r**2)

print(area(4))

fruits = ['apple', 'pear', 'cherry']
print(fruits)

elements = [1, 0.8, True, 'orange']
elements[2]
elements[-1]
elements[1:3]
# 0.8 and True will print (does not include 'orange')
elements[2] = 'pineapple'

