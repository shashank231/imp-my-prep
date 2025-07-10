
from typing import List


def aggressiveCows(stalls: List[int], k: int):
    stalls.sort()
    lenStalls = len(stalls)
    if lenStalls <= 1:
        return 0

    def isPossibleAnswer(minDist: int):
        # Most important thing that i was unable to understand here was this that 
        # we can always start assigning stall from 0, and by keeping the min_distance property always True
        lastCowPlaced = 0 
        cowsPlaced = 1
        for i in range(1, lenStalls):
            if (stalls[i]-stalls[lastCowPlaced]) >= minDist:
                cowsPlaced += 1
                lastCowPlaced = i
                if cowsPlaced == k:
                    return True
        return False
    
    left = 0
    right = sum(stalls)
    ans = right

    while(left<=right):
        mid = (left+right)//2
        isPossible = isPossibleAnswer(mid)
        if isPossible:
            ans = mid
            left = mid+1
        else:
            right = mid-1
    
    return ans


st = [2, 12, 11, 3, 26, 7]
k = 5

answ = aggressiveCows(st, k)
print(answ)






