# First version
def move_zeros(nums):
    for i in range(len(nums)):
        if (nums[i] == 0):
            nums.pop(i)
            nums.append(0)

    return nums
        
print(move_zeros([1,0,3,0,12]))

# Better version
def move_zeros2(nums2):
    j = 0
    for i in range(len(nums2)):
        if (nums2[i] != 0):
            nums2[i], nums2[j] = nums2[j], nums2[i]
            j += 1
    
    return nums2

print(move_zeros2([0,1,0,3,12]))
