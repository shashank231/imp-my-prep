


def subarraySum(nums, k):
    ansCount = 0
    l1 = len(nums)

    def helper(index, sm):
        nonlocal ansCount
        if index >= l1: return
        
        
        for i in range(index, l1):
            ele = nums[i]
            
            if i == index:
                newSm = sm + ele
            else:
                newSm = ele
                return

            if newSm == k:
                ansCount += 1
                return
            elif newSm < k:
                helper(i+1, newSm)
            else:
                helper(i+1, 0)


        
    
    helper(0, 0)
    return ansCount

a = subarraySum([-1, -1, 1], 1)

print(a)

