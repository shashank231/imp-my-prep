
# Input: bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
# Output: 12
# Explanation: We need 2 bouquets each should have 3 flowers.
# Here is the garden after the 7 and 12 days:
# After day 7: [x, x, x, x, _, x, x]
# We can make one bouquet of the first three flowers that bloomed. We cannot make another bouquet from the last three flowers that bloomed because they are not adjacent.
# After day 12: [x, x, x, x, x, x, x]
# It is obvious that we can make two bouquets in different ways.


def make_m_bouqets(bloomDay, m, k):
    """
    m: no. of bouqets
    k: adjacent flowers from garden needed for a bouqet 
    """

    left = 0
    right = max(bloomDay)
    ans = -1

    def isAllBouqetsPossible(days):
        arr = [1 if days>=d else 0 for d in bloomDay]
        num_bouqets = 0
        temp = 0
        for i in arr:
            if i==1:
                temp+=1
                if temp==k:
                    num_bouqets+=1
                    temp = 0
                    if num_bouqets >= m:
                        return True
            else:
                temp = 0
        return False

    while (left<=right):
        mid = (left+right)//2
        possible = isAllBouqetsPossible(mid)
        if possible:
            ans = mid
            right = mid-1
        else:
            left = mid+1
    return ans



blooms = [7,7,7,7,12,7,7]
m = 2
k = 3

answ = make_m_bouqets(blooms, m, k)
print("answ => ", answ)
