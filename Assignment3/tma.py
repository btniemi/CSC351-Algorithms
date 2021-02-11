import pytest

"""I used code from https://www.geeksforgeeks.org/stable-marriage-problem/ to help jumpstart my idea.
I modified things to match the parameters of the project."""

"""think nested 4 loops, use lists of lists, termination condition = all men have a mate
what to do last is to figure out the file read and file write
"""

m_preference = [[3,2,5,1,4],[1,2,5,3,4],[4,3,2,1,5],[1,3,4,2,5],[1,2,4,5,3]]
w_preference = [[3,5,2,1,4],[5,2,1,4,3],[4,3,5,1,2],[1,2,3,4,5],[2,3,4,1,5]]
marriages = [(1,5),(2,2),(3,4),(4,3),(5,1)] #(boys,girls) girls saying no and men seeking

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
                    # manPrime throws away his preference for that woman from his list as they will not match

                else:
                    """man prime and woman remain engaged"""
            i += 1
    return print(freeM, freeW, sep="\r\n")  # mess with this return statement to get a better print of pairings
                                            #print to a file the answer need help here to see if I am on the right path...




matched = [(1, 5), (2, 4), (3, 3), (4, 2), (5, 1)]

def check(matched):
    #for each boy first tuple
        #check if match equals any other matched boy tuples pair
            #if yes match == false
            #else match == true
    pass

match(m_preference, w_preference)
