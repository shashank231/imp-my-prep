

arr = [1, 4, 6, 8, 10, 14, 45, 67]

def upperBound(arr, ele):

    left = 0
    right = len(arr)-1
    ans = -1

    while (left <= right):
        mid = (left + right)//2
        if arr[mid] == ele:
            ans = arr[mid+1]
            break
        elif arr[mid] > ele:
            ans = arr[mid]
            right = mid-1
        else:
            left = mid+1
    
    print(ans)

upperBound(arr, 44)