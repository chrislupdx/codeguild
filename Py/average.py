#begin with a list, iterate through it
nums = [1, 2, 3, 4, 5, 6, 7, 8]
length = len(nums)
value = 0
# for i in nums:
    # value += i
    # value = value + i
value = sum(nums)

avg = value / length
print(avg)
