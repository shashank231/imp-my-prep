
# Case 1: Single Transaction (Leetcode #121)
# We want to buy at the lowest point before a higher point appears.

def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit

# Example
print(maxProfit([7,1,5,3,6,4]))  # Output: 5


# Time: O(n)
# Space: O(1)

# Intuition:
# Track the lowest price so far, and compute the profit if you sold today. Update the max profit whenever it improves.

# Case 2: Multiple Transactions Allowed (Leetcode #122)
# Buy low, sell high repeatedly (greedy approach).

def maxProfit(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit

# Example
print(maxProfit([7,1,5,3,6,4]))  # Output: 7 (buy 1->sell 5, buy 3->sell 6)


# Time: O(n)
# Space: O(1)



class Solution:
    
    def largetElementOnRight(self, arr):
        largestTillNow = -1
        lenArr = len(arr)
    
        largestOnRight = list()
        lastIndex = lenArr-1
    
        for i in range(lastIndex, -1, -1):
            if i == lastIndex:
                largestOnRight.append(-1)
                largestTillNow = arr[lastIndex]
            else:
                currEle = arr[i]
                if currEle > largestTillNow:
                    largestTillNow = currEle
                    largestOnRight.append(-1)
                else:
                    largestOnRight.append(largestTillNow)
    
        largestOnRight.reverse()
        return largestOnRight


    def maximumProfit(self, arr):
        largestOnRIght = self.largetElementOnRight(arr)
        maxa = 0
        l1 = len(arr)
    
        for i in range(l1):
            largestOnRightEle = largestOnRIght[i]
            if largestOnRightEle == -1:
                pass
            else:
                p1 = largestOnRightEle - arr[i]
                maxa = max(maxa, p1)

        return maxa
        
        

class Solution:

    def findMinimas(self, arr):
        if len(arr) == 1:
            return ["mi"]
        lenArr = len(arr)
        firstIndex = 0
        lastIndex = lenArr-1
        minimas = [0]*lenArr

        for index in range(lenArr):
            if index==firstIndex:
                if arr[index] < arr[index+1]:
                    minimas[index] = "mi"
            elif index==lastIndex:
                if arr[index] < arr[index-1]:
                    minimas[index] = "mi"
            else:
                if arr[index-1] > arr[index] and arr[index] < arr[index+1]:
                    minimas[index] = "mi"
        return minimas

    def findMaximas(self, arr):
        if len(arr) == 1:
            return ["mx"]
        lenArr = len(arr)
        firstIndex = 0
        lastIndex = lenArr-1
        maximas = [0]*lenArr
    
        for index in range(lenArr):
            if index==firstIndex:
                if arr[index] > arr[index+1]:
                    maximas[index] = "mx"
            elif index==lastIndex:
                if arr[index] > arr[index-1]:
                    maximas[index] = "mx"
            else:
                if arr[index-1] < arr[index] and arr[index] > arr[index+1]:
                    maximas[index] = "mx"
        return maximas

    def uniqueInOrder(self, arr):
        lenArr = len(arr)
        firstIndex = 0
        uniqueArr = list()
        uniqueArr.append(arr[firstIndex])
        for index in range(1, lenArr):
            currEle = arr[index]
            lastEleInUniqueArr = uniqueArr[-1]
            if currEle == lastEleInUniqueArr:
                pass
            else:
                uniqueArr.append(currEle) 
        return uniqueArr

    def maximumProfit(self, arr1):
        arr = self.uniqueInOrder(arr1)
        lenArr = len(arr)
        minimas = self.findMinimas(arr)
        maximas = self.findMaximas(arr)
        combined = minimas
        for i in range(len(maximas)):
            if maximas[i] == "mx":
                combined[i] = "mx"

        for i in range(lenArr):
            if combined[i] != 0:
                if combined[i] == "mx":
                    combined[i] = 0
                break    
        for i in range(lenArr-1, -1, -1):
            if combined[i] != 0: 
                if combined[i]=="mi":
                    combined[i] = 0
                break
    
        prices = []
        for i in range(lenArr):
            if combined[i] != 0:
                prices.append(arr[i])        
        answer = 0
        flag = True    
        for i in prices:
            if flag:
                answer -= i
                flag = False
            else:
                answer += i
                flag = True

        return answer

