

class Solution:
    memo1 = {}

    def fun3(self, arr_cuts, left, right):
        key = (left, right)
        if self.memo1.get(key):
            return self.memo1.get(key)


        min_cost_to_cut = float("inf")

        for i in range(len(arr_cuts)):
            point_of_cut = arr_cuts[i]
            if point_of_cut > left and point_of_cut < right:
                price = (right - left)
                cuts_left = arr_cuts[:i]+arr_cuts[i+1:]
                if cuts_left:
                    price1 = self.fun3(cuts_left, left, point_of_cut)
                    price2 = self.fun3(cuts_left, point_of_cut, right)
                    price += price1
                    price += price2
                min_cost_to_cut = min(
                    min_cost_to_cut,
                    price
                )
        if min_cost_to_cut == float("inf"):
            min_cost_to_cut = 0

        self.memo1[key] = min_cost_to_cut
        return min_cost_to_cut 


    def minCost(self, n, cuts) -> int:
        ans = self.fun3(cuts, 0, n)
        return ans



def fun11(arr, summ, start):
    ways = 0

    for i in range(start, len(arr)):
        coin_val = arr[i]
        sum_left = summ - coin_val
        if sum_left < 0:
            continue
        elif sum_left == 0:
            ways += 1
        else:
            ways += fun11(arr, sum_left, i)

    return ways

def fun12(arr, summ, start, answ):
    ways = 0

    for i in range(start, len(arr)):
        coin_val = arr[i]
        sum_left = summ - coin_val

        if sum_left < 0:
            continue
        elif sum_left == 0:
            ways += 1
            answ1 = answ + [coin_val]
            print(answ1)
        else:
            answ2 = answ + [coin_val]
            ways += fun12(arr, sum_left, i, answ2)

    return ways


ans1 = fun12([1, 2, 3], 5, 0, [])
print(ans1)














 