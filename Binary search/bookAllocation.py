
from typing import List

def findPages(self, arr, k):
    len_arr = len(arr)
    if len(arr) < k:
        return -1

    def isPossibleAnswer(maxPages: int) -> bool:
        students = 0
        assignedPages = 0
        index = 0

        while index < len_arr:
            if arr[index] > maxPages:
                return False
            assignedPages += arr[index]
            if assignedPages < maxPages:
                index += 1
            elif assignedPages == maxPages:
                students += 1
                if students > k:
                    return False
                index += 1
                assignedPages = 0
            else:
                students+=1
                if students > k:
                    return False
                assignedPages = 0

        if assignedPages>0 and assignedPages<=maxPages:
            students += 1
            if students > k:
                return False

        return True

    left = 0  
    right = sum(arr)
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if isPossibleAnswer(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans


arr = [15, 17, 20]
k = 5
