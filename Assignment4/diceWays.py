import pytest
from itertools import product

"""used code from https://www.geeksforgeeks.org/python-k-dice-combinations/ to get insight on list compression
and how to use the product() function from itertools, can use fstring or string format to pretty print answers
did not figure this out but will work on later"""


def num_ways(num_dice, num_faces, wanted_sum):
    num_ways_list = []
    # get a list of the possible values of num dice and faces
    dice_combos = list(product(range(1, num_faces + 1), repeat=num_dice))
    # iterate over that list to see if sums of those == wanted sum
    for items in dice_combos:
        if sum(items) == wanted_sum:
            # save to another list
            num_ways_list.append(items)
    # num ways = len of that list of saved possible outcomes
    num_ways_res = len(num_ways_list)
    # create a cool print statement that shows the list and the number of ways to return
    # want to do this to prove it works
    if wanted_sum < num_dice or wanted_sum > num_dice * num_faces:
        return 0
    else:
        return num_ways_res


def main():
    num_dice = int(input("How many dice do you have? "))
    num_faces = int(input("How many faces do those dice have? "))
    wanted_sum = int(input("What number are you trying to roll for? "))
    print(num_ways(num_dice, num_faces, wanted_sum))


if __name__ == "__main__":
    main()

"""tests still not working but the algo is completed not sure how to fix"""
def test_diceWays():
    assert num_ways(3, 6, 8) == 21, "should pass"
def test_diceWays():
    assert num_ways(3, 6, 1) == 0, "should pass"
def test_diceWays():
    assert num_ways(1, 6, 4) == 1, "should pass"
