def mover_zeros(nums):
    contador = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[contador] = nums[contador], nums[i]   
            contador += 1

    return nums