# Example showing how to trace a for-loop

def squareSums(n):
    '''list of the first n sums of squares'''
    L = []
    s = 0
    for i in range(1,n+1):
        s += i*i
        L.append(s)
    return L

# Draw the loop trace for squareSums

#test will have tracing of individual variables and the end return

# Below fill in the squareSumsTrace function as a self-tracing version of square Sums

def squareSumsTrace(n):
    '''self-tracing version of squareSums'''
    L = []
    s = 0
    print("i"+"\t"+"s"+"\t"+"L")
    print("--------------------")
    for i in range(1,n+1):
        s += i*i
        L.append(s)
        print(i,"\t",s,"\t",L)
    return L

squareSumsTrace(5)
