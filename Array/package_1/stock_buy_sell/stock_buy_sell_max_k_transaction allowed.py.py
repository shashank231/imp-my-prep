# https://www.geeksforgeeks.org/problems/maximum-profit4657/1

# 🚨 On any given day, you do NOT have 3 options.
# You only have 2 valid options depending on whether you are holding a stock or not.
# Let’s break the mental model fully so it becomes obvious and natural to you.

# ✅ Correct Mindset: You are either holding stock or not.
# At each day, the agent (you) is in one of these two states:

# 🧩 State 1 — You are NOT holding a stock
# This means:
# can_buy = True
# can_sell = False
# On this day, your valid actions are:
# ✔ Option A: Buy the stock
# ✔ Option B: Skip (do nothing)
# You cannot sell, because you don't have a stock yet.

# 🧩 State 2 — You ARE holding a stock
# This means:
# can_buy = False
# can_sell = True
# On this day, your valid actions are:
# ✔ Option A: Sell the stock
# ✔ Option B: Skip (do nothing)
# You cannot buy, because buying again before selling is illegal (no overlapping transactions).


def maxProfit(k, prices):
    n = len(prices)
    from functools import lru_cache

    @lru_cache(None)
    def dp(day, can_buy, trans_left):
        if day == n or trans_left == 0:
            return 0
        
        if can_buy:
            # Option1: Buy
            buy = -prices[day] + dp(day + 1, False, trans_left)
            # Option2: Skip
            skip = dp(day + 1, True, trans_left)
            return max(buy, skip)
        else:
            # Option1: Sell
            sell = prices[day] + dp(day + 1, True, trans_left - 1)
            # Option2: Hold
            hold = dp(day + 1, False, trans_left)
            return max(sell, hold)

    return dp(0, True, k)


prices = [10, 22, 5, 80]
k = 2

ans = maxProfit(k, prices)
print(ans)


# def fun1(
#     prices, 
#     max_trans, 
#     total_days,
#     can_buy=True,
#     can_sell=False,
#     last_buy_price=-1,
#     num_trans_complete=0, 
#     day=1,
# ):
#     # option1: buy
#     profit1 = 0
#     if can_buy:
#         buying_price = prices[day-1]
#         if num_trans_complete < max_trans and day+1 < total_days:
#             profit1 = fun1(prices, max_trans, total_days, False, True, buying_price, num_trans_complete, day+1)

#     # option2: sell
#     profit2 = 0
#     if can_sell:
#         selling_price = prices[day-1]
#         if day+1 < total_days:
#             profit2 = (selling_price-last_buy_price) + fun1(prices, max_trans, total_days, True, False, -1, num_trans_complete+1, day+1)

#     # option3: hold
#     profit3 = 0
#     if day+1 < total_days:
#         profit3 = fun1(prices, max_trans, total_days, can_buy, can_sell, last_buy_price, num_trans_complete, day+1)

#     return max(profit1, profit2, profit3)



# 🔥 Why "buy / sell / skip" as 3 options is WRONG
# Because the buy and sell operations are mutually exclusive:
# If you haven't bought yet → selling is invalid
# If you are holding stock → buying again is invalid
# Your function tried to do:
# profit = max(buy_option, sell_option, skip_option)


# But:
# Sometimes "sell_option" was illegal
# Sometimes "buy_option" was illegal
# You allowed both to exist in same day
# Which can lead to “double selling” or “double buying” problems
# This corrupts state transitions.
