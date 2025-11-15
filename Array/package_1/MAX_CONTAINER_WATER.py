
# https://www.geeksforgeeks.org/problems/container-with-most-water0535/1


# 3️⃣ Optimized Two Pointers (O(n)) ✅
# Here’s the trick:

# Start with two pointers: left = 0, right = n-1.
# Calculate area = (right - left) × min(height[left], height[right]).
# Move the pointer with the smaller height inward (because moving the larger one inward cannot possibly get a larger area).
# Repeat until left < right.

# Why This Works
# The width shrinks as we move inward, so to maximize area, we must try to increase the height. The only way to potentially get a larger area is by moving the pointer at the shorter line inward.


def maxArea(height):
    left, right = 0, len(height) - 1
    max_area = 0
    
    while left < right:
        # Calculate area
        width = right - left
        min_height = min(height[left], height[right])
        area = width * min_height
        max_area = max(max_area, area)
        
        # Move the smaller height pointer inward
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area

# Example
height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))  # Output: 49


# 4️⃣ Complexity
# Time: O(n) (one pass with two pointers)
# Space: O(1) (no extra memory)
