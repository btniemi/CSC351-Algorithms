count = 10**5
nums = []

# this is fast as it is only one step per calculation
for i in range(count):
    nums.append(i)

print(nums.reverse())
nums.reverse()


# this below grows quadratically so it takes longer
nums = []
for i in range(count):
    nums.insert(0, i)