# https://www.geeksforgeeks.org/problems/rotate-array-by-n-elements-1587115621/1

class Solution:

    def rotateArr(self, arr, d):
        lenArr = len(arr)
        normalized_d = d%lenArr
        arr.reverse()

        left = lenArr - normalized_d
        right = lenArr - 1
        while (left <= right):
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        left1 = 0
        right1 = lenArr - normalized_d - 1
        while (left1 <= right1):
            arr[left1], arr[right1] = arr[right1], arr[left1]
            left1 += 1
            right1 -= 1
        
        return arr


