
# Question: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/


import math
from typing import List

def shipWithinDays(weights: List[int], days:int) -> int:
    len_weights = len(weights)
    max_capacity = sum(weights)

    def valueAt(index):
        return weights[index]
    
    def ispossibleAnswer(capacity: int) -> bool:
        days_needed = 0
        shipped = 0

        index=0
        while (index<len_weights):
            shipped += valueAt(index)
            if shipped < capacity:
                index += 1
            elif shipped==capacity:
                days_needed += 1
                if days_needed > days:
                    return False
                index += 1
                shipped = 0
            else:
                shipped -= valueAt(index)
                if shipped > 0:
                    days_needed += 1
                    if days_needed > days:
                        return False
                    shipped = 0
                else:
                    return False
        
        if shipped and shipped>0 and shipped<=capacity:
            days_needed += 1
            shipped = 0
            if days_needed > days:
                return False

        return True
    
    left = 0
    right = max_capacity
    ans = max_capacity

    while (left<=right):
        mid = (left+right)//2
        possible = ispossibleAnswer(mid)
        if possible:
            ans = mid
            right = mid-1
        else:
            left = mid+1
    
    return ans


w1 = [1,2,3,4,5,6,7,8,9,10]
d1 = 5

answ = shipWithinDays(w1, d1)
print(answ)






