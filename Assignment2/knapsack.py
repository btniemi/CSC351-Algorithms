import pytest

""" I used code from https://www.geeksforgeeks.org/fractional-knapsack-problem/ to help kickstart my ideas,
ended up useing most of the same code and tried to make it different but could not find another way. Not
suer if there is a simpler way to do this???"""


# used a class here as you need to be able to carry variable all the way through the program.
class ItemValue:
    def __init__(self, weight, value, index):
        self.weight = weight
        self.value = value
        self.index = index
        self.cost = weight / value

    # this is an override for the greater than symbol so that you can compare two object class types
    def __gt__(self, other):
        return self.cost > other.cost


def fillKnapsackByValue(items, capacity):
    weight = []
    value = []
    for i in items:
        value.append(i[0])
        weight.append(i[1])
    print(weight)
    print(value)

    if len(weight) != len(value):
        raise Exception("Sorry, not every items weight has a corresponding value.")

    iVal = []
    for i in range(len(weight)):
        iVal.append(ItemValue(weight[i], value[i], i))
    iVal.sort()

    totalValue = 0
    for i in iVal:
        curWt = int(i.weight)
        curVal = int(i.value)
        if capacity - curWt >= 0:
            capacity -= curWt
            totalValue += curVal
        else:
            fraction = capacity / curWt
            totalValue += curVal * fraction
            capacity = int(capacity - (curWt * fraction))
            break
    return totalValue

knapsack = 50
file = open("myItems.txt", "r")
itemsList = file.read()
print(itemsList)

maxValue = fillKnapsackByValue(itemsList, knapsack)
print("The max value of your bag is: ", maxValue)


# I cant figure out how to write a test case for this to actually work honestly I dont understand how to write test at all (its like its not working at all honestly)
def test_knapsack():
    assert fillKnapsackByValue([(60, 10), (40, 40), (100, 20), (120, 30)], 50) == 240, "Should PASS"
def test_knapsack():
    assert fillKnapsackByValue([(60, 20), (40, 40), (100, 20), (120, 30)], 50) == 220, "Should PASS"
def test_knapsack():
    assert fillKnapsackByValue([(60, 30), (40, 40), (100, 20), (120, 30)], 50) == 220, "Should PASS"
def test_knapsack():
    assert fillKnapsackByValue([(60, 10), (40, 20), (100, 10), (120, 10)], 50) != 240, "Should Pass but is the failing test case"
