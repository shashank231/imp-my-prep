

class Solution:

    def fun3(self, arr_cuts, left, right):

        min_cost_to_cut = float("inf")
        
        for i in range(len(arr_cuts)):
            point_of_cut = arr_cuts[i]
            if point_of_cut > left and point_of_cut < right:
                price = right - left
                cuts_left = arr_cuts[:i] + arr_cuts[i + 1 :]
                if cuts_left:
                    price1 = self.fun3(cuts_left, left, point_of_cut)
                    price2 = self.fun3(cuts_left, point_of_cut, right)
                    price += price1
                    price += price2
                min_cost_to_cut = min(min_cost_to_cut, price)
        
        if min_cost_to_cut == float("inf"):
            min_cost_to_cut = 0

        return min_cost_to_cut


    def minCost(self, n1, cuts1) -> int:
        ans = self.fun3(cuts1, 0, n1)
        return ans