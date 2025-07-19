
# https://leetcode.com/problems/rotate-array/
class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n  # In case k > n

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        reverse(0, n - 1)       # Reverse entire array
        reverse(0, k - 1)       # Reverse first k elements
        reverse(k, n - 1)       # Reverse the rest
