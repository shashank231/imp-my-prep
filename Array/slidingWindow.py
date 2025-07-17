import heapq


def fun1(arr, batch):
    lenArr = len(arr)
    if batch >= lenArr:
        return sum(arr)

    start = 0
    end = batch-1
    answer = -1
    newSum = sum(arr[start:end+1])

    for end in range(end+1, lenArr):
        newSum = newSum + arr[end] - arr[start]
        answer = max(newSum, answer)
        start += 1

    print(answer)


# fun1([10, 76, 56, 78, 96, 34, 54, 100, 100, 100, 65, 78], 3)


def fun2(arr, k):
    window = arr[:k]
    start = 0
    end = k-1
    lenArr = len(arr)
    heapq.heapify(window)
    minSubArr = list()
    minSubArr.append(window[0])

    while (end < lenArr):
        if end == k-1:
            end = end+1
            continue
        heapq.heappush(window, arr[end])
        # heapq.heappop(window, arr[start])
        window.remove(arr[start])
        minVal = window[0]
        minSubArr.append(minVal)
        start = start+1
        end = end+1
    
    print(minSubArr)


fun2([1, 2, -1, 3, -2, 4, 5, 6, 2, 4, -34, 10], 3)




    




    