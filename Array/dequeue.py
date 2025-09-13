from collections import deque


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


# https://www.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k3345/1
class Solution:
    
    def firstNegInt(self, arr, k):
        queue = deque([])
        answer = list()

        for i in range(k):
            if arr[i] < 0:
                queue.append(i)
        if queue:
            answer.append(arr[queue[0]])
        else:
            answer.append(0)


        for end in range(k, len(arr)):
            while queue and queue[0] < end-k+1:
                queue.popleft()
            if arr[end] < 0:
                queue.append(end)
            if queue:
                answer.append(arr[queue[0]])
            else:
                answer.append(0)

        return answer


# https://www.geeksforgeeks.org/problems/first-non-repeating-character-in-a-stream1216/1
class Solution:
    def FirstNonRepeating(self, s):
        checkDict = dict()
        answer = ""
        dq = deque()

        for ch in s:
            checkDict[ch] = checkDict.get(ch, 0) + 1
            dq.append(ch)

            # remove repeating chars from front
            while dq and checkDict[dq[0]] > 1:
                dq.popleft()

            if dq:
                answer += dq[0]
            else:
                answer += "#"

        return answer


