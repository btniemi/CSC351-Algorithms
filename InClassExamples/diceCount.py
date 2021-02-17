def find_ways(dice, sides, total):
    num_ways = 0
    if total == dice:
        return 1
    if total < dice or total > (dice * sides):
        return 0
    if dice == 1:
        if total <= sides:
            return 1

    for i in range(1, sides + 1):
        num_ways += find_ways(dice - 1, sides, total - i)

    return num_ways

print(find_ways(3,6,8))