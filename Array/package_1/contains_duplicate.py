
# https://leetcode.com/problems/contains-duplicate-ii/submissions/1837881446/

# IN THIS QUESTION K=3, THIS IS SLIDING WINDOW PROBLEM, NEVER MISS 


class Solution(object):
    
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        set1 = set()
        dict1 = dict()
        firstoccurence = dict()
        for index, ele in enumerate(nums):
            if ele in set1:
                if ele in dict1:
                    dict1[ele].append(index)
                else:
                    dict1[ele] = [firstoccurence[ele], index]
            else:
                set1.add(ele)
                firstoccurence[ele] = index
        
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
