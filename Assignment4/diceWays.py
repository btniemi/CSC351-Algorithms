import pytest
from itertools import product

"""need to add the cmd line functionality with sys.argv stuff and the main etc see about this in class friday
will probably have to reformat a bunch of stuff to dumb it down but this works really well as implementation
don't even need to check side cases etc with list compression included"""

num_dice = int(input("How many dice do you have? "))
num_faces = int(input("How many faces do those dice have? "))
wanted_sum = int(input("What number are you trying to roll for? "))


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
    return print("There are", num_ways_res, "ways to roll", wanted_sum, "from", num_dice, "dice with", num_faces,
                 "faces and they are:\n", num_ways_list)


num_ways(num_dice, num_faces, wanted_sum)

"""this test probably wont work because I am returning a print statement from the function ask about in class"""
def test_diceWays():
    assert num_ways(3, 6, 8) == 21
