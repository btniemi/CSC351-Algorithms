"""used code from https://realpython.com/sorting-algorithms-python/#the-bubble-sort-algorithm-in-python
as a guide to the algorithms basically a copy of those and how they work"""

from random import randint
from timeit import repeat

ARRAY_LENGTH = 10

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j+1], array[j]
                already_sorted = False
        if already_sorted:
            break
    return array

def insertion_sort(array):
    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1
        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item
    return array

def merge_sort(array):
    if len(array) < 2:
        return array
    midpoint = len(array) // 2
    left = merge_sort(array[:midpoint])
    right = merge_sort(array[midpoint:])
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left
    result = []
    index_left = index_right = 0
    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1
        if index_right == len(right):
            result += left[index_left:]
            break
        if index_left == len(left):
            result += right[index_right:]
            break
    return result

def quick_sort(array):
    if len(array) < 2:
        return array
    low, same, high = [], [], []
    pivot = array[randint(0, len(array) - 1)]
    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)
    return quick_sort(low) + same + quick_sort(high)


def time_sorting_algorithm(algorithm, array):
    if algorithm == "sorted":
        setup_code = ""
    else:
        setup_code = f"from __main__ import {algorithm}"

    stmt = f"{algorithm}({array})"

    # Executes the code ten times and return the time in seconds that each execution took
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")


if __name__ == "__main__":
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]

    time_sorting_algorithm(algorithm="bubble_sort", array=array)
    time_sorting_algorithm(algorithm="insertion_sort", array=array)
    time_sorting_algorithm(algorithm="merge_sort", array=array)
    time_sorting_algorithm(algorithm="quick_sort", array=array)
    time_sorting_algorithm(algorithm="sorted", array=array)