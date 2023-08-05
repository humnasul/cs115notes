def change(x, y, z):
    x += 1
    y += [5]
    z[4] = 5

num = 6
li = [1,2,3]
z = {1:2, 5:2}

change(num, li, z)

print(num, li, z)


y = list(li)
y[0] = 4

print(id(li[0]))
print(id(y[0]))

y[0] = 1

print(li)
print(y)

print(id(li[0]))
print(id(y[0]))

'''
y = []

for x in li:
    y += [x]

print(li)
print(y)

print(id(y[0]))
print(id(li[0]))
'''
