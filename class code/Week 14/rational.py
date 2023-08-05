class Rational:
    def __init__(self, n, d):
        if d == 0:
            raise ZeroDivisionError("Denom.cannot be zero")
        else:
            self.numerator = n
            self.denominator = d
    def isZero(self):
        return self.numerator == 0
    def __str__(self):
        #becomes default for printing object - you need the double underscores before and afer for it to become default
        return str(self.numerator)+"/"+str(self.denominator)

    def __eq__(self, other):
        return self.numerator * other.denominator == self.denominator * other.numerator

    def equals(self, other):
        return self.numerator * other.denominator == self.denominator * other.numerator

    def __add__(self, other):
        newNumerator = self.numerator * other.denominator + self.denominator * other.numerator
        newDenominator = self.denominator * other.denominator
        return Rational(newNumerator, newDenominator)
    ''' allows you to call like + between two objects instead of .add()'''
    def __ge__(self, other):
        return self.numerator * other.denominator >= self.denominator * other.numerator

myNum1 = Rational(1,3)
# myNum1 is an object from the class Rationals
print(myNum1.numerator)
myNum2 = Rational(2,6)
print(myNum2.denominator)
num1 = Rational(1,3)
num2 = Rational(1,3)
print(num1 == num2)
# different memory addresses, so returns false
print(id(num1))
print(id(num2))
#different addresses!!
num1 = Rational(0,6)
print(num1.isZero())
num1 = Rational(1,3)
print(num1)
#prints object address normally, but __str__ makes a different default print for the object
myNum1 = Rational(1,3)
myNum2 = Rational(2,6)
print(myNum1 == myNum2)
print(myNum1.equals(myNum2))

myNum1 = Rational(36,1000)
myNum2 = Rational(6, 1000)
myNum3 = myNum1 + myNum2
print(myNum3)

result = Rational(42, 1000)
print(myNum3 == result)

myNum3 = Rational(42, 1000)
print(myNum1 + myNum2 >= myNum3)
