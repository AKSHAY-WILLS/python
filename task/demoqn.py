nums = [-2,-1,1,10,2,3,2,4,5,3,5]
num = sorted(nums, key=lambda x: (abs(x), -x))[0]
print(f"closest to zero is {num}")