##def main()
## '''The main recommendation function -- pseudocode'''
##    userPrefs = loadUsers(PREF_FILE)
##    print welcome
##    get username
##    get user preferences
##    get recommendations
##    print them, if there are any
##    save userPrefs into PREF_FILE

def loadUsers(filename):
    dic = {}
    with open(filename, "r") as f:
        for line in f:
            [username, singers] = line.strip().split(":")
            singersList = singers.split(",")
            dic[username] = singersList
    return dic


def numMatches(userPrefs, storedUserPrefs):
    ''' return the number of elements that match between
        the lists userPrefs and storedUserPrefs. O(mn)
    '''
    count = 0
    for item in userPrefs:
        if item in storedUserPrefs:
            count += 1
    return count




def numMatchesFast(userPrefs, storedUserPrefs):
    ''' return the number of elements that match between
        the lists userPrefs and storedUserPrefs. O(nlogn)
    '''
    x = list(userPrefs)
    x.sort()
    y = list(storedUserPrefs)
    y.sort()
    i,j, cnt = 0,0,0
    while i < len(x) and j < len(y):
        if x[i] == y[j]:
            cnt += 1
            i += 1
            j += 1
        elif x[i] > y[j]:
            j += 1
        else:
            i += 1
    return cnt

    
    
