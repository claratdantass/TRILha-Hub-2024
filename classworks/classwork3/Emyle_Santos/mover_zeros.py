def mover_zero(nums):
    for x in range(len(nums)):
        if nums[x] == 0:
            y = nums.pop(x)
            nums.append(y)
    return nums

nums = [0,1,0,3,12] 

print(mover_zero(nums))
