

# https://leetcode.com/problems/longest-mountain-in-array/

class Solution:
    def longestMountain(self, arr):
        """
        A mountain is defined as:
        - strictly increasing sequence
        - followed by strictly decreasing sequence
        - minimum length = 3

        We expand outward from every peak.
        """

        n = len(arr)
        longest = 0

        # A valid peak must be between 1 and n-2
        for i in range(1, n - 1):

            # Check if current index is a peak: arr[i-1] < arr[i] > arr[i+1]
            if arr[i - 1] < arr[i] > arr[i + 1]:

                left = i
                right = i

                # Expand left while strictly increasing towards the peak
                while left > 0 and arr[left] > arr[left - 1]:
                    left -= 1

                # Expand right while strictly decreasing away from the peak
                while right < n - 1 and arr[right] > arr[right + 1]:
                    right += 1

                # Mountain length = right - left + 1
                longest = max(longest, right - left + 1)

        return longest

