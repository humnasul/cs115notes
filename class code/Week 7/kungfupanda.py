dic = {1:1, 2:2, 3:4}
# number of steps associated with number of ways to do the problem

def KFP_slow(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return KFP_slow(n-1) + KFP_slow(n-2) + KFP_slow(n-3)
#slower function

    
def KFP_fast(n):
    if n in dic:
        return dic[n]
    ans = KFP_fast(n-1)
    dic[n-1] = ans
    ans2 = KFP_fast(n-2)
    dic[n-2] = ans2
    ans3 = KFP_fast(n-3)
    dic[n-3] = ans3
    return ans + ans2 + ans3

import time
def MeasureTime(f, n):
    start = time.time()
    f(n)
    return time.time() - start

print("KFP slow takes:", round(MeasureTime(KFP_slow, 30),6), "secs")
print("KFP fast takes:", round(MeasureTime(KFP_fast, 30),6), "secs")
