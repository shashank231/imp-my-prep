
# https://leetcode.com/problems/contains-duplicate-ii/submissions/1837881446/

# IN THIS QUESTION K=3, THIS IS SLIDING WINDOW PROBLEM, NEVER MISS 
# The sliding window approach to this problem is very interesting 
# yt at that time: https://youtu.be/lvO88XxNAzs?t=5192

class Solution(object):
    
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict1 = dict()
        for index, ele in enumerate(nums):
            if ele in dict1:
                dict1[ele].append(index)
            else:
                dict1[ele] = [index]
        answr = False
        for key in dict1:
            value = dict1[key]
            for ind in range(1, len(value)):
                d1 = value[ind] - value[ind-1]
                if d1 <= k:
                    answr = True
                    break
        return answr


a1 = Solution().containsNearbyDuplicate([1, 2, 3, 1], 3)

print(a1)
