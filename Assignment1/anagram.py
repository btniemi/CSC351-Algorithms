# used https://www.geeksforgeeks.org/python-sorted-check-two-strings-anagram-not/ as a guide for this program
"""dont really need the print statements in here unless you feel like they help you understand.
 Could probably just comment that out or add a comments to help understand what going on"""


def anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if len(s1) == len(s2):
        if (sorted(s1) == sorted(s2)):
            print("YES, is anagram.")
            return True
        else:
            print("No, NOT anagrams.")
            return False
    elif len(s1) != len(s2):
        print("No, NOT anagrams.")
        return False


def test_anagram():
    assert anagram("listen","silent") == True
def test_anagram():
    assert anagram("blaga","blaau") == False
def test_anagram():
    assert anagram("goodness gracious", "blue") == False
def test_anagram():
    assert anagram("bad credit", "debit card") == True
def test_anagram():
    assert anagram("Bad CreDit", "Debit CaRd") == True

