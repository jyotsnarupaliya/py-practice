def threeSum(nums):
    #nums.sort()
    result = set()
    for i in range(len(nums)):
        a = nums[i]
        visited = set()
        b_plus_c = 0 - a
        for j in range(i+1, len(nums)):
            # logic for two sum
            b = nums[j]
            c = b_plus_c - b
            triplet = (b, a, c)
            if c in visited:
                result.add(tuple(sorted(triplet)))
            visited.add(b)
    return result
    
print(threeSum([-1,0,1,2,-1,-4]))
