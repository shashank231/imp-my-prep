
class Solution:
	
    def pushZerosToEnd(self, arr):
        lenArr = len(arr)
        firstIndex = 0
        lastIndex = lenArr-1
        nextNonZeroEleIndex = 0

        for index in range(lenArr):
            currEle = arr[index]
            if currEle != 0:
                arr[nextNonZeroEleIndex], arr[index] = arr[index], arr[nextNonZeroEleIndex]
                nextNonZeroEleIndex += 1
        
        return arr




a1 = [0, 0, 0, 3, 1, 4]
s1 = Solution().pushZerosToEnd(a1)
print(s1)




    	