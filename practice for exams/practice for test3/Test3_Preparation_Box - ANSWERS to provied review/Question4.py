"""
    Question 4 of Test3 Sample
    Author: Zumrut Akcam-Kibis
"""

def draw(n):
    for i in range(1, n+1):
        if i == 1 or i == n:
            print("*"*n)
        else:
            print("*"+" "*(n-2)+"*")

if __name__ == "__main__":
    n = int(input("Enter a number to draw a square with that side length: "))
    draw(n)
