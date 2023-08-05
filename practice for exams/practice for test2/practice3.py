def listProd(L,M):
    if len(L) == 0 and len(M) == 0:
        return []
    if len(L) == 0 and len(M) != 0:
        #you actually don't need to check if the other list is != 0
        return M[0:]
    if len(M) == 0 and len(L) != 0:
        return L[0:]
    else:
        return [L[0]*M[0]] + listProd(L[1:], M[1:])

print(listProd([1,2,3], [6,5,4,9,8,7]))
print(listProd([1,2,3], [1,2,3]))   
