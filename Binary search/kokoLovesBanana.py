# Que: https://leetcode.com/problems/koko-eating-bananas/description/
# Intution
# Whenever we have questions like up to a certain point the answers are possible and after a certain point answer is not possible
# we can always apply binary search in such cases

# Iss case me hume minimum no. of bananas per hour find karna hai
# we will start from max and check if ans is possible for mid
# if possible for mid we will set mid for now and proceed

import math

def kokoLovesBanana(piles, h):
    left = 0
    right = max(piles)
    ans = right

    def possibleToEat(k):
        time = 0
        for p in piles:
            time += math.ceil(p/k)
            if time > h:
                return False
        return True

    while(left<=right):
        mid = (left+right)//2
        possible = possibleToEat(mid)
        if possible:
            ans = mid
            right=mid-1
        else:
            left=mid+1
    
    return ans

p1 = [30,11,23,4,20]
h1 = 6
ans = kokoLovesBanana(p1, h1)
print(ans)

