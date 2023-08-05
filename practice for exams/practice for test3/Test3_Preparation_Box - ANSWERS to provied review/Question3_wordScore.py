"""
    Question 4 of Test3 Sample
    Author: Zumrut Akcam-Kibis
"""
letterScores = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2}

def wordScore (S):
    '''Assume S is a string . Return the scrabble score of S, using letterScores .
    For letters not in letterScores , the score is 0.
    For example , wordScore (" eagle ") is 5 (i.e., 1 + 1 + 2 + 0 + 1). '''
    if S == '':
        return 0
    elif S[0] in letterScores:
        return letterScores[S[0]] + wordScore(S[1:])
    else:
        return wordScore(S[1:])

def wordScoreLoop(S):
    total = 0
    for letter in S:
        if letter in letterScores:
            total += letterScores[letter]
    return total

print(wordScore("eagle"))
print(wordScoreLoop("eagle"))
