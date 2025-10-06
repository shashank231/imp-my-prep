# https://www.geeksforgeeks.org/problems/find-missing-and-repeating2512/1


class Solution:

    def findTwoElement(self, arr):
        lenArr = len(arr)
        dict1 = {}
        for i in range(1, lenArr+1):
            dict1[i] = 0
        
        for i in arr:
            dict1[i] += 1
        
        miss, rep = -1, -1
        for i in range(1, lenArr+1):
            if dict1[i] == 0:
                miss = i
            if dict1[i] == 2:
                rep = i
        
        return [rep, miss]


a1 = [4, 3, 6, 2, 1, 1]
Solution().findTwoElement(a1)



                 


