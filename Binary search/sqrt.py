# https://leetcode.com/problems/sqrtx/description/
# Intution: 
# Whenever we have questions like up to a certain point the answers are possible and after a certain point answer is not possible
# we can always apply binary search in such cases

def funSqrt(x):
    left = 0
    right = x
    ans = -1

    while(left <= right):
        mid = (left+right)//2
        midSqr = mid*mid
        if midSqr==x:
            ans = mid
            break
        if midSqr < x:
            ans = mid # mid can be an answer as we are not sure like (mid+1)**2 can be greater than x, so keep the best for now and proceed
            left = mid+1
        else:
            right = mid-1
    return ans

ans = funSqrt(0)
print(ans)

def funPower(x, power):
    left = 0
    right = x
    ans = -1

    while(left <= right):
        mid = (left+right)//2
        midSqr = mid**power
        if midSqr==x:
            ans = mid
            break
        if midSqr < x:
            ans = mid 
            left = mid+1
        else:
            right = mid-1
    return ans

