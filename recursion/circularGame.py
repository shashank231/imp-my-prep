

class Solution(object):
    
    def fun1(self, n, steps, start):
        end = start + steps
        rem = end % n
        if rem == 0:
            return n-1
        return rem-1

    def nextStart(self, n, possibleNextStart):
        if possibleNextStart==n:
            return 0
        return possibleNextStart
    
    def solve(self, n, steps, start, arr):
        lenArr = len(arr)
        if lenArr==1:
            return arr[0]
        
        indexOfFriendToBeRemoved = self.fun1(n, steps, start)
        newStart = indexOfFriendToBeRemoved
        if newStart == lenArr-1:
            newStart = 0
        newArr = arr[:indexOfFriendToBeRemoved]+arr[indexOfFriendToBeRemoved+1:]
        return self.solve(n-1, steps, newStart, newArr)

    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        arr = [i for i in range(1, n+1)]
        return self.solve(n, k, 0, arr)

a = Solution().findTheWinner(6, 5)
print(a)


# Function to find the maximum sum of a contiguous subarray in a given integer array
def kadane(A):
 
   # find the maximum element present in a given list
   # if the list contains all negative values, return the maximum element
    maximum = max(A)
    if maximum < 0:
        return maximum
 
    # stores the maximum sum sublist found so far
    max_so_far = 0
    # stores the maximum sum of sublist ending at the current position
    max_ending_here = 0
 
    # do for each element of a given list
    for i in A:
        # update the maximum sum of sublist "ending" at index `i` (by adding the
        # current element to maximum sum ending at previous index `i-1`)
        max_ending_here = max_ending_here + i
 
        # if the maximum sum is negative, set it to 0 (which represents
        # an empty sublist)
        max_ending_here = max(max_ending_here, 0)
 
        # update the result if the current sublist sum is found to be greater
        max_so_far = max(max_so_far, max_ending_here)
 
    return max_so_far
 
 
if __name__ == '__main__':
 
    A = [-8, -3, -6, -2, -5, -4]
    print("The sum of contiguous sublist with the largest sum is", kadane(A))
 
