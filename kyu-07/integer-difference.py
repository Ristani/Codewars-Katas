def int_diff(nums, n):
    result = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if abs(nums[i] - nums[j]) == n:
                result += 1
    return result
