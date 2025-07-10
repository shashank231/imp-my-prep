import pdb
from typing import List
from pprint import pprint
from collections import Counter
# que: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
class Solution1:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        len1 = len(numbers)
        left = 0
        right = len1-1
        solved = False

        while (True):
            sum_pointers = numbers[left] + numbers[right]
            if sum_pointers == target:
                solved = True
                break
            elif sum_pointers > target:
                right = right-1
            else:
                left = left+1

        return (left+1, right+1)


# https://leetcode.com/problems/container-with-most-water/submissions/1686162011/
class Solution2:

    def maxArea(self, height: List[int]) -> int:
        maxArea = float("-inf")
        len1 = len(height)
        left = 0
        right = len1-1

        while (left <= right):
            maxArea = max(
                maxArea,
                (right-left) * min(height[left], height[right])
            )
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
        
        return maxArea


# https://leetcode.com/problems/3sum/
class Solution3:

    def main(self, nums, ans_list):
        len_ans_list = len(ans_list)
        if len_ans_list == 3:
            if sum(ans_list) == 0:
                self.solution.append(ans_list)
                return
            return

        for index in range(len(nums)):
            num = nums[index]
            new_nums = nums[index+1:]
            new_ans_list = ans_list + [num]
            self.main(new_nums, new_ans_list)

        return

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self.solution = list()
        self.main(nums, [])
        partial_Solution = self.solution
        normalized = [tuple(sorted(triplet)) for triplet in partial_Solution]
        unique = set(normalized)
        result = [list(triplet) for triplet in unique]
        return result


# https://leetcode.com/problems/minimum-window-substring/description/
class Solution4:

    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        t_count = Counter(t)
        window_counts = {}        
        have, need = 0, len(t_count)
        res, res_len = [-1, -1], float("inf")


        left = 0
        for right in range(len(s)):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1            
            # If current char count matches the required count in t
            if char in t_count and window_counts[char] == t_count[char]:
                have += 1

            # Try to shrink the window
            while have == need:
                # Update result if smaller window is found
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1
                
                # Shrink from the left
                window_counts[s[left]] -= 1
                if s[left] in t_count and window_counts[s[left]] < t_count[s[left]]:
                    have -= 1
                left += 1
        

        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""



        






        


