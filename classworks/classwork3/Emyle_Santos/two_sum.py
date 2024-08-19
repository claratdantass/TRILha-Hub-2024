def two_sum(nums,k):
    for i in range(len(nums)):
        for j in range(i + 1,len(nums)):
                if(nums[i] + nums[j] == k):
                    print(True)
                    result = (nums[i],nums[j])
                    return result
                    
nums = [1,2,3,4,5]
k = 9

result = two_sum(nums,k)
print(result)
