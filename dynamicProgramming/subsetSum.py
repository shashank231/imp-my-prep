from functools import lru_cache

class Solution:
    def canPartition(self, arr):
        total = sum(arr)
        if total % 2 != 0:
            return False
        target = total // 2

        @lru_cache(maxsize=None)
        def helper(i, curr_sum):
            if curr_sum == target:
                return True
            if curr_sum > target or i >= len(arr):
                return False

            return helper(i+1, curr_sum + arr[i]) or helper(i+1, curr_sum)  # ********
        
        return helper(0, 0)













class Solution:

    def canPartition(self, arr):
        memo = dict()

        def helper(arr, target):
            key = (tuple(arr), target)
            if memo.get(key):
                return memo[key]

            for index in range(len(arr)):
                ele = arr[index]
                newTarget = target-ele
                newArr = arr[:index] + arr[index+1:]
                if newTarget < 0:
                    continue
                elif newTarget == 0:
                    memo[key] = True
                    return True
                else:
                    bool1 = helper(newArr, newTarget)
                    if bool1:
                        memo[key] = bool1 
                        return bool1
            memo[key] = False
            return False

        totalSum = sum(arr)
        if totalSum % 2 != 0:
            return False
        else:
            halfSum = totalSum//2
            partitionPossible = helper(arr, halfSum)
            return partitionPossible
