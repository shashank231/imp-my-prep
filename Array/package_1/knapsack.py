
def fun11(arr, summ):
    ways = 0
    lenArr = len(arr)

    def helper(idx, currSum, ans):
        nonlocal ways
        if currSum == summ:
            print(ans)
            ways += 1
            return
        if currSum > summ or idx >= lenArr:
            return

        ele = arr[idx]
        newCurrSum = currSum + ele
        newAns = ans + [ele]

        # helper(idx, newCurrSum, newAns)   # Repetion aloud order doesn't matter
        # helper(0, newCurrSum, newAns)     # Repetion aloud order matter         1️⃣ take element → repetition allowed → restart at 0
        helper(idx+1, newCurrSum, newAns)   # No Repetition No Order

        helper(idx + 1, currSum, ans)

    helper(0, 0, [])
    return ways



# No repetition, order matters
def fun_no_repeat_order(arr, summ):
    ways = 0
    lenArr = len(arr)

    def helper(used, currSum, ans):
        nonlocal ways
        if currSum == summ:
            print(ans)
            ways += 1
            return
        if currSum > summ:
            return
        # loop because order matters → try every remaining element
        for i in range(lenArr):
            if used[i]:
                continue
            ele = arr[i]
            newCurrSum = currSum + ele
            newAns = ans + [ele]
            used[i] = True       # mark taken (no repetition)
            helper(used, newCurrSum, newAns)
            used[i] = False      # backtrack

    helper([False] * lenArr, 0, [])
    return ways

