memo = {}

def fun1(lengths, prices, n):
    if memo.get(n):
        return memo[n]

    max_profit = -1
    for i in range(len(lengths)):
        cut_length = lengths[i]
        cut_price = prices[i]

        if cut_length == n:
            max_profit = max(
                max_profit,
                cut_price + 0,
            )
        elif cut_length < n:
            remaining_length = n - cut_length
            max_profit_remaining_rod = fun1(lengths, prices, remaining_length)
            max_profit = max(
                max_profit,
                cut_price + max_profit_remaining_rod,
            )
        else: # cut_length > n
            max_profit = max(
                max_profit,
                0 + 0, 
            )
    
    memo[n] = max_profit
    return max_profit

def fun2(prices):
    N = len(prices)
    lengths = [i+1 for i in range(N)]
    ans = fun1(lengths, prices, N)
    return ans

# ========================

n = 7
cuts = [1, 3, 4, 5]


memo1 = {}

def fun3(arr_cuts, left, right):
    key = (left, right)
    if memo1.get(key):
        return memo1.get(key)

    min_cost_to_cut = float("inf")
    for i in range(len(arr_cuts)):
        point_of_cut = arr_cuts[i]
        if point_of_cut > left and point_of_cut < right:
            price = (right - left)
            cuts_left = arr_cuts[:i]+arr_cuts[i+1:]
            if cuts_left:
                price1 = fun3(cuts_left, left, point_of_cut)
                price2 = fun3(cuts_left, point_of_cut, right)
                price += price1
                price += price2
            min_cost_to_cut = min(
                min_cost_to_cut,
                price
            )
    if min_cost_to_cut == float("inf"):
        min_cost_to_cut = 0
    memo1[key] = min_cost_to_cut
    return min_cost_to_cut 
        

        
ans1 = fun3([5, 6, 1, 4, 2], 0, 9)
print(ans1)
