menPreference = [['C','B','E','A','D'], ['A','B','E','C','D'],['D','C','B','A','E'],['A','C','D','B','E'],['A','B','D','E','C']]
womenPreference = [[3,5,2,1,4],[5,2,1,4,3],[4,3,5,1,2],[1,2,3,4,5],[2,3,4,1,5]]

def match(men, women):
    #initilize all men and women to free
    #where there is a free man who has a woman to purpose to:
        #w=m highest ranked choice that he has not yet purposed to
        #if this woman is free:
            #man and woman get engaged
        #else woman is engaged to man prime
            #if woman prefers man to man prime
                #man and woman get engaged
                #man prime set to free
            #else:
                #man prime and woman remain engaged

def check(matched):
    #use the match function to check if pairings are bad or not correct this should be a basic call to the match function i think

"""think nested 4 loops,
can pop from a list,
 use lists of lists,
 termination condition = all men have a mate
 what to do last is to figure out the file read and file write
"""