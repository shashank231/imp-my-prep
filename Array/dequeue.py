from collections import deque


# https://www.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k3345/1
class Solution:
    
    def firstNegInt(self, arr, k):
        dq = deque()
        result = []

        for i in range(k):
            if arr[i] < 0:
                dq.append(i)
        if dq:
            result.append(arr[dq[0]])
        else:
            result.append(0)        


        for end in range(k, len(arr)):
            while dq and dq[0] < end-k+1:
                dq.popleft()
            if arr[end] < 0:
                dq.append(end)
            if dq:
                result.append(arr[dq[0]])
            else:
                result.append(0)
        
        return result





class Solution:

    def  maxSlidingWindow(self, arr, k):
        dq = deque()
        result = []

        # Process first k elements
        for i in range(k):
            while dq and arr[i] >= arr[dq[-1]]:    # | deque se pop kro 
                dq.pop()                           # |

            dq.append(i)                           # | deque me dalo
        result.append(arr[dq[0]])

        
        # Process the rest of the array
        for end in range(k, len(arr)):
            # Remove indices outside the current window
            while dq and dq[0] < end - k + 1:                   # | window adjust karo
                dq.popleft()

            # Remove smaller elements from the back             # | deque se pop karo 
            while dq and arr[end] >= arr[dq[-1]]:
                dq.pop()

            dq.append(end)                                      # | deque mein dalo
            result.append(arr[dq[0]])

        
        return result

        