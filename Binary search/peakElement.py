
# link: https://leetcode.com/problems/find-peak-element/description/
# Find peak in mountain array, there can be mutiple peaks but upword and downward trend is always mantained

def findPeakElement(arr):
    len_arr = len(arr)
    left = 0
    right = len_arr-1
    ans = 0

    while (left <= right):
        mid = (left + right)//2
        if (mid+1) < len_arr:
            if arr[mid+1] < arr[mid]:
                ans = mid
                right = mid-1
            elif arr[mid+1] == arr[mid]:
                ans = mid
                break
            else:
                left = mid+1
        elif (mid-1) >= 0:
            if arr[mid-1] < arr[mid]:
                ans = mid
                left = mid+1
            elif arr[mid-1] == arr[mid]:
                ans = mid
                break
            else:
                right = mid-1
        else:
            ans = mid
            break

    return ans

def findPeakElement2(arr) -> int:
        len_arr = len(arr)
        left = 0
        right = len_arr-1
        ans = -1

        def isValid(index):
            if index>=0 and index<len_arr:
                return True
            return False
        
        def valueAt(index):
            return arr[index]

        def isPeak(index):
            flag = True
            if isValid(index-1):
                if valueAt(index-1)>valueAt(index):
                    flag = False
            if isValid(index+1):
                if valueAt(index+1)>valueAt(index):
                    flag = False
            return flag


        while(left <= right):
            mid = (left+right)//2
            if isPeak(mid):
                ans = mid
                break
            # You may think here that what if mid+1 is invalid for this array
            # but there is a very imporatnt intution here
            # For mid+1 to be invalid "mid" should be last element isse pichli(current-1) call me.. 
            #   if mid peak hua to isPeak handle kar lega and return kar dega so this invalid mid+1 would be never called
            #   else mid peak nahi hua, to usse pichli(current-2) call kabhi last element ko mid banne he nahi degi
            if valueAt(mid+1)>valueAt(mid):
                left = mid+1
            else:
                right = mid

        return ans
