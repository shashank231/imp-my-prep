
# Que link
# https://leetcode.com/problems/single-element-in-a-sorted-array/description/
# Main thought process came when we realized that arr was sorted


def findSingleEle(arr):
    len_arr = len(arr) 
    left = 0
    right = len_arr-1
    ans = -1

    def isValid(index):
        if index>=0 and index < len_arr:
            return True
        return False
    
    def isEven(index):
        if index==0:
            return True
        if index%2==0:
            return True
        return False

    while(left <= right):
        mid = (left+right)//2
        same_val_index = -1
        if isValid(mid-1) and arr[mid-1]==arr[mid]:
            same_val_index = mid-1
        if isValid(mid+1) and arr[mid+1]==arr[mid]:
            same_val_index = mid+1
        if same_val_index==-1:
            ans = mid
            break
        
        first_occurence_index = min(mid, same_val_index)
        is_first_occurence_index_even = isEven(first_occurence_index)
        if is_first_occurence_index_even:
            left=mid+1
        else:
            right=mid-1
    
    if ans==-1:
        return ans
    return arr[ans]

arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 6]
ans = findSingleEle(arr)
print(ans)





