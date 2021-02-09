import pytest

"""I used code from https://www.geeksforgeeks.org/stable-marriage-problem/ to help jumpstart my idea.
I modified things to match the parameters of the project."""

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
    m = 0

    #where there is a free man who has a woman to purpose to:
    while m < freeCount:
        if freeM[m] == False:
            break
        m += 1
    # w=m highest ranked choice that he has not yet purposed to
    i = 0
    while i < freeCount and freeM[m] == False:
        w = menPrefrence[m][i]
        #if this woman is free:
        if freeW[w] == False:
            # man and woman get engaged
            freeW[w] = m
            freeM[m] = True
            freeCount -= 1
        #else woman is engaged to man prime
        else:
            mPrime = freeW[w]
            #if woman prefers man to man prime
            if womanPrefrence[w][m] < womanPrefrence[w][mPrime]:
                freeW[w] = m
                # man and woman get engaged
                freeM[m] = True
                # man prime set to free
                freeM[mPrime] = False
            else:
                #man prime and woman remain engaged
                break
        i += 1

    #print to a file the answer need help here to see if I am on the right path...

def check(matched):
    #use the match function to check if pairings are bad or not correct this should be a basic call to the match function i think

    """think nested 4 loops,
    can pop from a list,
    use lists of lists,
    termination condition = all men have a mate
    what to do last is to figure out the file read and file write
    """

match(m_preference, w_preference)