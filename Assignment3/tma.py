#import pytest
import sys
import ast

"""I used code from https://www.geeksforgeeks.org/stable-marriage-problem/ to help jumpstart my idea.
I modified things to match the parameters of the project."""

"""think nested 4 loops, use lists of lists, termination condition = all men have a mate
what to do last is to figure out the file read and file write
"""
if sys.argv[1] == "match":
    """MATCH FUNCTION BELOW"""
    def match(menPrefrence, womanPrefrence):
        if len(menPrefrence) != len(womanPrefrence):
            raise Exception("Sorry, pairing cant be made lists are not equal")
        #initilize all men and women to free
        count = len(menPrefrence)
        freeM = [False for i in range(count)]
        freeW = [False for i in range(count)]
        freeCount = len(freeM)
        n = freeCount
        #where there is a free man who has a woman to purpose to:
        while freeCount > 0:
            m = 0
            while m < n:
                if freeM[m] == False:
                    break
                m += 1
        #w=m highest ranked choice that he has not yet purposed to
            i = 0
            while i < n and freeM[m] == False:
                w = menPrefrence[m][i]
                #if this woman is free:
                if freeW[w-1] == False:
                    # man and woman get engaged
                    freeW[w-1] = m + 1
                    freeM[m] = True
                    freeCount -= 1
                #else woman is engaged to man prime
                else:
                    mPrime = freeW[w-1]
                    prime = womanPrefrence[w-1].index(mPrime)
                    newMan = m + 1
                    man = womanPrefrence[w-1].index(newMan)
                    #if woman prefers man to man prime
                    if man < prime:
                        freeW[w-1] = newMan
                        # man and woman get engaged
                        freeM[m] = True
                        # man prime set to free
                        freeM[mPrime-1] = False
                    else:
                        """man prime and woman remain engaged nothing happens"""
                i += 1
        j = 0
        ans = []
        for i in range(n):
            ans.append((j+1, int(freeW[j])))
            j += 1
        return ans

    if(len(sys.argv)>=3):
        with open(sys.argv[2], 'r') as f1:
            m_pref = f1.readlines()
            m_pref = ast.literal_eval(m_pref[0])
        with open(sys.argv[3], 'r') as f2:
            w_pref = f2.readlines()
            w_pref = ast.literal_eval(w_pref[0])
    else:
        print("you do not have enough arguments")

    men = m_pref
    women = w_pref
    matchedPairs = match(men, women)
    print(matchedPairs, "also they are stored in tmaMatches.txt")

    with open('tmaMatches.txt', 'w') as matchedFile:
        stringMatched = matchedFile.writelines(str(matchedPairs))

elif sys.argv[1] == "check":
    """CHECK FUNCTION BELOW"""
    def check(matches):
        count = len(matches)
        checkList = [False for i in range(count)]
        for items in matches:
            checkList[items[1]-1] = True
        if False in checkList:
            indx = checkList.index(False)
            return "Not a stable match, rogue couples found ", indx, " does not have a match"
        else:
            return "Yes! Stable match, no rogue couples found"

    if(len(sys.argv)>=2):
        with open(sys.argv[2], 'r') as f3:
            c_Marriage = f3.readlines()
            c_Marriage = ast.literal_eval(c_Marriage[0])
    else:
        print("you do no have enough arguments")

    c_file = c_Marriage
    print(check(c_file))

else:
    print("please enter a valid argument")

"""stuff below is for testing purposes"""
m_preference = [[3,2,5,1,4],[1,2,5,3,4],[4,3,2,1,5],[1,3,4,2,5],[1,2,4,5,3]]
w_preference = [[3,5,2,1,4],[5,2,1,4,3],[4,3,5,1,2],[1,2,3,4,5],[2,3,4,1,5]]
marriages = [(1,5),(2,2),(3,4),(4,3),(5,1)] #(boys,girls) girls saying no and men seeking used for testing purposes
matched = [(1, 5), (2, 4), (3, 3), (4, 2), (5, 1)] #works
matched2 = [(1, 5), (2, 4), (3, 3), (4, 3), (5, 1)] #does not work

"""tests do not work at all and not sure why. cant get them to work one time during development.
does it have to do with sys.argv???"""
def test_tma():
    assert match(m_preference, w_preference) == marriages, "should pass"
def test_tma():
    assert check(matched) == True, "should pass"
def test_tma():
    assert check(matched2) == False, "should not pass"