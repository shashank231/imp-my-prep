

def largetElementOnRight(arr):

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

def main(arr):
    largestOnRIght = largetElementOnRight(arr)
    maxa = 0
    l1 = len(arr)
    # ar1 = []

    for i in range(l1):
        largestOnRightEle = largestOnRIght[i]
        if largestOnRightEle == -1:
            # ar1.append(0)
            pass
        else:
            p1 = largestOnRightEle - arr[i]
            # ar1.append(p1)
            maxa = max(maxa, p1)
    
    # print(maxa)
    # print(ar1)

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

