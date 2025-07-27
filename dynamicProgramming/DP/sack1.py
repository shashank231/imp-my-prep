from functools import lru_cache


def fun1(arr, sm):
    ways = 0
    lenArr = len(arr)

    def helper(index, target, ans):
        nonlocal ways
        if target == sm:
            print(ans)
            ways += 1
            return
        if target > sm or index >= lenArr:
            return

        ele = arr[index]
        newTarget = target + ele
        newAns = ans + [ele]
        helper(index+1, target, ans)
        helper(index, newTarget, newAns)

    helper(0, 0, [])
    return ways


def fun2(arr, sm):
    ways = 0
    lenArr = len(arr)

    def helper(target, ans):
        nonlocal ways
        if target == sm:
            print(ans) 
            ways += 1
            return
        if target > sm:
            return

        for i in range(lenArr):
            ele = arr[i]
            newTarget = target + ele
            newAns = ans + [ele]
            helper(newTarget, newAns)

    helper(0, [])
    return ways


def fun3(arr, sm):
    ways = 0
    lenArr = len(arr)

    def helper(index, target, ans):
        nonlocal ways
        if target == sm:
            print(ans)
            ways += 1
            return
        if target > sm or index >= lenArr:
            return

        ele = arr[index]
        newTarget = target + ele
        newAns = ans + [ele]
        helper(index+1, newTarget, newAns)
        helper(index+1, target, ans)

    helper(0, 0, [])
    return ways


def fun4(arr, sm):
    ways = 0
    lenArr = len(arr)

    def helper(arr, target, ans):
        nonlocal ways
        if target == sm:
            print(ans)
            ways += 1
            return
        if target > sm or not arr:
            return

        for i in range(len(arr)):
            ele = arr[i]
            newArr = arr[:i] + arr[i+1:]
            newTarget = target + ele
            newAns = ans + [ele]
            helper(newArr, newTarget, newAns)

    helper(arr, 0, [])
    return ways

def fun41(arr, sm):
    ways = 0
    lenArr = len(arr)
    used = [False] * lenArr  # 👈 mark if element is already used

    def helper(target, ans):
        nonlocal ways
        if target == sm:
            print(ans)
            ways += 1
            return
        if target > sm:
            return

        for i in range(lenArr):
            if not used[i]:
                used[i] = True           # ✅ mark element as used
                helper(target + arr[i], ans + [arr[i]])
                used[i] = False          # 🔄 backtrack

    helper(0, [])
    return ways


arr = [1, 2, 3]
sm = 6
print("Total unique combinations with Repetition position don't matter:")
fun1(arr, sm)


print("Total unique combinations with Repetition position matter:")
fun2(arr, sm)


print("Total unique combinations without Repetition position don't matter:")
fun3(arr, sm)


print("Total unique combinations without Repetition position matter:")
fun41(arr, sm)

