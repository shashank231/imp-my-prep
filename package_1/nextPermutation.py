
import copy


class Solution:

    def nextPermutation(self, arr):
        is_reverse_sorted = all(arr[i] >= arr[i+1] for i in range(len(arr)-1))
        if is_reverse_sorted:
            return arr.sort()

        lenArr = len(arr)
        firstIndex = 0
        lastIndex = lenArr-1
        breakPoint = 0
        for index in range(lastIndex, -1, -1):
            nextIndex = index-1
            if arr[nextIndex] < arr[index]:
                breakPoint = nextIndex
                break

        firstPart = arr[:breakPoint]
        secondPart = arr[breakPoint:]

        firstEleSecdPart = secondPart[0]
        secondPartCopy = copy.deepcopy(secondPart)
        secondPartCopy.sort()
        finalSecondPart1 = []
        finalSecondPart2 = []
        firstBigFound = False
        for index1 in range(len(secondPartCopy)):
            curr = secondPartCopy[index1]
            added = False
            if curr > firstEleSecdPart:
                if not firstBigFound:
                    firstBigFound = True
                    added = True
                    finalSecondPart1.append(curr)
            if not added:
                finalSecondPart2.append(curr)
    
        soln = firstPart + finalSecondPart1 + finalSecondPart2
        arr[:] = soln
        return arr
