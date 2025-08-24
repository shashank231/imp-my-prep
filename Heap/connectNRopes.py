import heapq


def minCostToConnectNRopes(arr):
    n = len(arr)
    if n == 1:
        return 0   # no cost when only one rope left

    solution = float("inf")
    # try all pairs of ropes
    for i in range(n):
        for j in range(i+1, n):
            # combine ropes i and j
            cost = arr[i] + arr[j]
            newArr = [arr[k] for k in range(n) if k != i and k != j]
            newArr.append(cost)
            # recurse
            totalCost = cost + minCostToConnectNRopes(newArr)
            solution = min(solution, totalCost)
    return solution


arr = [4, 3, 2, 6]
print(minCostToConnectNRopes(arr))  # Output: 29


def connectRopes(arr):
    heapq.heapify(arr)
    minSum = 0

    while (len(arr) > 2):
        a = heapq.heappop(arr)
        b = heapq.heappop(arr)
        print(a, b)
        minSum += (a+b)
        heapq.heappush(arr, (a+b))
    
    print(minSum + sum(arr))

ar1 = [4, 3, 2, 6]
connectRopes(ar1)
