# Que: https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/description/
# Intution 
# Whenever you don't know how to approach but it seems like if you assume an answer, then you can surely
# check that if that no. is answer or not
# Essentially you dont know how to get answer.. but you can write a fn to check if a particular no. is answer or not.. plus
# you can negate the left or right side of answer depending upon whether the answer was possible or not..
# In such cases we can use Binary search by slowly approaching answer


import math
from typing import List

def smallestDivisor(
    nums: List[int],
    threshold: int
) -> int:
    left = 0
    right = max(nums)+1
    ans = right

    def isPossibleAnswer(a: int) -> bool:
        if a==0:
            return False
        sum_divisions = 0
        for n in nums:
            sum_divisions += math.ceil(n/a)
            if sum_divisions > threshold:
                return False
        return True

    while(left<=right):
        mid = (left+right)//2
        possible = isPossibleAnswer(mid)
        if possible:
            ans = mid
            right = mid-1
        else:
            left = mid+1
    
    return ans
