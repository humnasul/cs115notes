"""
Question 2 of Test3 Preparation Box
"""
def numMatches(L1, L2):
    '''return the number of elements that match between two sorted lists'''
    i = 0
    j = 0
    matches = 0
    print("i"+"\t"+"j"+"\t"+"matches")
    print(i,"\t",j,"\t",matches)
    while i < len(L1) and j < len(L2):
        if L1[i] == L2[j]:
            matches += 1
            i += 1
            j += 1
        elif L1[i] < L2[j]:
            i += 1
        else:
            j += 1
        print(i,"\t",j,"\t",matches)
    return matches

M1 = ["Chance", "DJ Shadow", "Khaled", "Meshell Ndegeocello", "St Vincent", "Travi$"]
M2 = ["Alicia Keys", "Chance", "Khaled", "Lila Downs", "Meshell Ndegeocello"]
numMatches(M1, M2)
