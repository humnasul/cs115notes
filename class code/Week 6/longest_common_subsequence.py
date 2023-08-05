def LCS(S1, S2):
    if S1 == "" or S2 == "":
        return 0
    else:
        if S1[0] == S2[0]:
            return 1 + LCS(S1[1:], S2[1:])
        else:
            useRight = LCS(S1[1:], S2)
            useLeft = LCS(S1, S2[1:])
            max(useRight, useLeft)
'''
    elif S1 == S2:
        return S1
    elif S1[0] == S2[0]:
        useRight = S2[0] + LCS(S, S2[1:])
        useLeft = S1[0] + LCS(S1[1:], S2)
        return
    else:
        return LCS(S1[1:], S2[1:])

print(LCS("sam!", "spam"))
'''
