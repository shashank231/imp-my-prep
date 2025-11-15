
class Solution:
    
    def removeDuplicates(self, arr):
        lenArr = len(arr)
        if lenArr == 1:
            return arr
        firstIndex = 0
        lastIndex = lenArr-1
        lastUniqueElement = arr[firstIndex]
        answer = list()
        answer.append(arr[firstIndex])
    
        index = firstIndex+1
        while (index <= lastIndex):
            currEle = arr[index]
            if currEle == lastUniqueElement:
                index += 1
            else:
                answer.append(currEle)
                lastUniqueElement = currEle
                index += 1
    
        return answer

