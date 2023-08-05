###########################################################################
# Question 1  [assess: encoding]
# This table defines a boolean function, f, of three arguments.
#
#    x | y | z | f(x,y,z)
#    --------------------
#    0 | 0 | 0 | 0
#    0 | 0 | 1 | 0
#    0 | 1 | 0 | 0
#    0 | 1 | 1 | 1
#    1 | 0 | 0 | 1
#    1 | 0 | 1 | 0
#    1 | 1 | 0 | 0
#    1 | 1 | 1 | 1        
# 
# Complete the following Python implementation of f, using a single return.
# Use the built-in Python functions "and", "or", "not".
# Hint: use the minterm expansion principle.
#
# SOLUTION is below, obtained by the minterm expansion principle.
# Here are the true rows:
#    0 | 1 | 1 | 1
#    1 | 0 | 0 | 1
#    1 | 1 | 1 | 1        
# So we make a 3-way 'or' using 'and' within each row.

###########################################################################

def f(x, y, z):
    # return None # TODO
    return (not x and y and z) or (x and not y and not z) or (x and y and z)



###########################################################################
# Question 2:  [assess: encoding]
# Part A: What is the two's complement representation of 29 in six bits?
# 
#    A: 011111 
#    B: 000111
#    C: 011101   
#    D: 000101
#
#
# ANSWER = C

###########################################################################
# Part B: What is the two's complement representation of -23 in six bits?
#
#    A: 101001
#    B: 110110
#    C: 110111
#    D: 010111
#
# ANSWER = A
###########################################################################
# Part C: Using two's complement with six bits, what is the largest
# positive number that can be represented, and what is the smallest (most negative)?
#
# LARGEST = 31, which is 2**5 - 1 (either answer is fine)
# 
# SMALLEST = -32, which is -(2**5)
###########################################################################
# Part D: Write your answers from part C in two's complement with six bits.
#
# LARGEST = 011111
# 
# SMALLEST = 100000
############################################################################ 


###########################################################################
# Question 3: [assess: coding]
# Complete the following function, using recursion on the lists.  That means 
# you can only access L using the expressions L[0], L==[], and L[1:].  And
# the same for M.  
#
# Hint: It can be done with one recursive call, where both lists are smaller.

###########################################################################

def listProd(L,M):
    '''Assume L and M are lists of  numbers.  Return a list of their products
    at corresponding indexes.  If one list is longer than the other, include its 
    elements at the end.  See testProd for examples.'''

    if L == []:
        return M
    elif M == []: return L
    else:
        return [ L[0]*M[0] ] + listProd(L[1:], M[1:])

def testProd():
    assert listProd([1,2,3], [1,2,3]) == [1, 4, 9]
    assert listProd([1,5,1], [2,3,3]) == [2,15,3]
    assert listProd([], [1,3,5,7]) == [1,3,5,7]
    assert listProd([1,2,3], [6,5,4,9,8,7]) == [6,10,12,9,8,7]


###########################################################################
# Question 4: (20 points) [assess: design]
# Below is an implementation of the longest common subsequence function.
# Add memoization.  
# Hint: create the dictionary in the main function, so you can refer to it
# in the code you add to LCShelp.
#
# SOLUTION - see "added" lines in the code below
# RUBRIC 5 initialize + 5 use table + 5 add new entries to table + 5 correct answers
#
###########################################################################
memo = {} #added - initialize the dictionary
def LCS(S1, S2):
    '''Length of the longest common subsequence of strings S1, S2.'''

    if (S1,S2) in memo:       # added - using the table
        return memo[(S1,S2)]  # added 
    elif S1 == "" or S2 == "": 
        result = 0
    elif S1[0] == S2[0]:
        result = 1 + LCS(S1[1:], S2[1:])
    else:
        chopS1 = LCS(S1[1:], S2)
        chopS2 = LCS(S1, S2[1:])
        result = max(chopS1, chopS2)
    memo[(S1,S2)] = result            # added - add new entries 
    return result


def testLCS():
    assert LCS("sam","spam!") == 3
    assert LCS("veto", "vote") == 2
    assert LCS("tranquil", "trail") == 5

###########################################################################
# Question 5: (15 points) [assess: execution]
# Write out the trace of function calls starting from fab(4,3) for the
# function defined below.
# Use indentation to indicate which calls are the result of preceding calls.
#
# Hint: You are welcome to modify the function and make it trace itself.
# But to answer the question you need to write your trace in the comment below.
# 
# SOLUTION - see below.  I've added a function fabT that prints its own trace,
# but you just need to write the trace in a comment.
###########################################################################

def fab(n,k):
    '''mystery function'''
    if n == 0 or n == 1:
        return k
    else:
        return fab(n-2,k) + fab(n-1,k)

def fabT(n,k):
    '''self-tracing fab'''
    def fabH(n,k,depth):
        print(i*'  ', "fab(", n, ",", k, ")")
        if n == 0 or n == 1:
            return k
        else:
            return fabH(n-2,k,depth+1) + fabH(n-1,k,depth+1)
    
    return fabH(n,k,0)


'''
TODO - your trace goes here

 fab(4,3)
   fab(2,3)
     fab(0,3)
     fab(1,3)
   fab(3,3)
     fab(1,3)
     fab(2,3)
       fab(0,3)
       fab(1,3)

'''




