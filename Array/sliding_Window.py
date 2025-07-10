


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


fun1([10, 76, 56, 78, 96, 34, 54, 100, 100, 100, 65, 78], 3)




    