


def search(arr, eleToSearch):
    lenArr = len(arr)
    left = 0
    right = lenArr-1
    ans = -1

    while (left <= right):
        mid = left + (right - left) // 2
        mid_val = arr[mid]
        if mid_val==eleToSearch:
            ans = mid
            break

        left_val = arr[left]
        right_val = arr[right]

        # find which side is sorted
        leftSideSorted = False
        if mid_val >= left_val:
            leftSideSorted = True

        if leftSideSorted:
            if eleToSearch>=left_val and eleToSearch<mid_val:
                right = mid-1
            else:
                left = mid+1

        if not leftSideSorted:
            if eleToSearch<=right_val and eleToSearch>mid_val:
                left = mid+1
            else:
                right = mid-1

    return ans


arr = [2, 3, 4, 5, 1]

search(arr, 1)




 