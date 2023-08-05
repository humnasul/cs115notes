def special(x):
    if x >= 42:
        print("Hi")
        return "Great number"
    elif x >= 7:
        print("Hoho")
        return "Another great number"
        #return leaves the function, so the bottom code only happens if the whole loop is false (nothing was returned)
    print("Hey")
    return "Not so great number"

def even(x):
    return x%2 == 0

def addTwoDigits(n):
    return n // 10 + n % 10

def largestNumber(n):
    return 10**n-1

print(special(45))
print(special(7))
print(special(15))

print(list(filter(even, [1,2,3,4])))
