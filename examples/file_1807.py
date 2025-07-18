nums = [1, 2, 3, 4]
length: int = len(nums)

i = 0

while True:
    index = i % length

    print(nums[index])

    if i == 10:
        break

    i += 1
