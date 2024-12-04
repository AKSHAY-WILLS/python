nums = [0, 1, 2, 4, 5, 7]
i = 0
result = []

while i < len(nums):
    begin = nums[i]
    while i < len(nums) - 1 and nums[i] == nums[i + 1] - 1:
        i += 1
    end = nums[i]
    
    if begin == end:
        result.append(str(begin))
    else:
        result.append(str(begin) + "->" + str(end))
    
    i += 1

print(result)