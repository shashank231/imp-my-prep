
# Problem link
# https://www.geeksforgeeks.org/problems/trapping-rain-water-1587115621/1


class Solution:
    
    def maxOnLeft(self, arr):
        lenArr = len(arr)
        answer = list()
        currMax = arr[0]
        currMaxIndex = 0
        answer.append(currMaxIndex)
        for index in range(1, lenArr):
            currEle = arr[index]
            if currEle > currMax:
                currMax = currEle
                currMaxIndex = index
            answer.append(currMaxIndex)
        return answer

    def maxOnRight(self, arr):
        lenArr = len(arr)
        lastIndex = lenArr-1
        answer = list()
        currMax = arr[-1]
        currMaxIndex = lastIndex
        answer.append(currMaxIndex)
    
        for index in range(lastIndex-1, -1, -1):
            currEle = arr[index]
            if currEle > currMax:
                currMax = currEle
                currMaxIndex = index
            answer.append(currMaxIndex)
    
        answer.reverse()
        return answer
    
    def maxWater(self, arr):
        lenArr = len(arr)
        maxLeft = self.maxOnLeft(arr)
        maxRight = self.maxOnRight(arr)
        firstIndex = 0
        lastIndex = lenArr-1
        maxWaterAns = 0
        
        for index in range(lenArr):
            maxOnLeftIndex = maxLeft[index]
            maxOnRightIndex = maxRight[index]
            ml = arr[maxOnLeftIndex]
            mr = arr[maxOnRightIndex]
            curr = arr[index]
            if index==firstIndex or index==lastIndex:
                continue
            min_l_r = min(ml, mr)
            water = min_l_r - curr
            maxWaterAns += water
        
        return maxWaterAns
    
