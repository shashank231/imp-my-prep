

class Solution:

    def threeSum(self, nums):
        """
        Return all unique triplets [i, j, k] such that: nums[i] + nums[j] + nums[k] == 0
        Uses sorting + two-pointer approach.
        """

        nums.sort()
        triplets = []
        n = len(nums)

        # Iterate each number as the first element of the triplet
        for i, val in enumerate(nums):

            # Skip duplicates for the first position
            if i > 0 and val == nums[i - 1]:
                continue

            left = i + 1               # Second element pointer
            right = n - 1              # Third element pointer

            # Two-pointer search for pairs that sum to -val
            while left < right:

                current_sum = val + nums[left] + nums[right]

                if current_sum > 0:
                    # Sum too large → decrease right to reduce sum
                    right -= 1

                elif current_sum < 0:
                    # Sum too small → increase left to increase sum
                    left += 1

                else:
                    # Found a valid triplet
                    triplets.append([val, nums[left], nums[right]])

                    left += 1  # move left pointer

                    # Skip duplicates for the second element
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return triplets

