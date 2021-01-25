string1 = "listen"
string2 = "silent"

string3 = "blaga"
string4 = "blaau"

string5 = "goodness gracious"
string6 = "wow"

string7 = "bad credit"
string8 = "debit card"

string9 = "Bad credit"
string10 = "Debit card"


# used https://www.geeksforgeeks.org/python-sorted-check-two-strings-anagram-not/ as a guide for this program

def anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if len(s1) == len(s2):
        if (sorted(s1) == sorted(s2)):
            print("YES, is anagram.")
        else:
            print("No, NOT anagrams.")
    elif len(s1) != len(s2):
        print("No, NOT anagrams.")


anagram(string1, string2)
anagram(string5, string6)
anagram(string3, string4)
anagram(string7, string8)
anagram(string9, string10)
