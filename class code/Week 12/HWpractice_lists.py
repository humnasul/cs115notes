def f(L):
    mult = L.copy()
    for i in range(1, len(L)-1):
        L[i] = (mult[i-1] + mult[i+1] + mult[i]) / 3
    return L

print(f([1,2,3,4,5]))
