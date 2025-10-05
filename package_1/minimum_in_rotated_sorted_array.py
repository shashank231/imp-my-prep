# https://www.geeksforgeeks.org/problems/minimum-element-in-a-sorted-and-rotated-array3611/1

class Solution:

    def findMin(self, arr):
        lenArr = len(arr)
        firstIndex = 0
        lastIndex = lenArr-1
        answer = float("inf")

        left = firstIndex
        right = lastIndex

        while (left <= right):
            mid = left + (right - left) // 2
            midVal = arr[mid]
            left_val = arr[left]
            right_val = arr[right]
            
            leftSideSorted = False
            if midVal >= left_val:
                leftSideSorted = True

            if leftSideSorted:
                answer = min(left_val, answer)
                left = mid+1
            else:
                answer = min(midVal, answer)
                right = mid-1
        
        return answer
