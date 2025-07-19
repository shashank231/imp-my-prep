


def fun(arr):

    lastUniqueElementIndex = 0

    j = 1

    while (j < len(arr)):
        if arr[j] == arr[lastUniqueElementIndex]:
            j += 1
        else:
            arr[lastUniqueElementIndex+1], arr[j] = arr[j], arr[lastUniqueElementIndex+1]
            lastUniqueElementIndex += 1
            j += 1
    
    print(arr)

fun([1, 1, 1, 1, 2, 2, 3, 4, 5, 6, 6, 6, 6, 6, 7, 7, 7, 8, 8])
