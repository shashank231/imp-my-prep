import pdb
from typing import List
from pprint import pprint


arr = [1, 3, 0, 0, 1, 2, 4]


def nearestGreaterToRight(arr):
    print(arr)
    answerArr = []
    stack = []

    for end in range(len(arr)-1, -1, -1):
        if not(stack):
            answerArr.append(-1)
        elif stack[-1] > arr[end]:
            answerArr.append(stack[-1])
        else:
            added = False
            while stack:
                ele = stack[-1]
                if ele > arr[end]:
                    answerArr.append(ele)
                    added = True
                    break
                else:
                    stack.pop()
            if not added:
                answerArr.append(-1)
        stack.append(arr[end])
    
    print(answerArr[::-1])


def nearestGreaterToLeft(arr):
    print(arr)
    answerArr = []
    stack = []

    for end in range(0, len(arr)):
        curr = arr[end]
        if not stack:
            answerArr.append(-1)
        elif stack[-1] > curr:
            answerArr.append(stack[-1])
        else:
            added = False
            while stack:
                ele = stack[-1]
                if ele > curr:
                    answerArr.append(ele)
                    added = True
                    break
                else:
                    stack.pop()
            if not added: 
                answerArr.append(-1)

        stack.append(curr)


    print(answerArr)


def nearestSmallestRight(arr):
    print(arr)
    answerArr = []
    stack = []

    for end in range(len(arr)-1, -1, -1):
        if not stack:
            answerArr.append(-1)
        elif stack[-1] < arr[end]:
            answerArr.append(stack[-1])
        else:
            added = False
            while(stack):
                ele = stack[-1]
                if ele < arr[end]:
                    answerArr.append(ele)
                    added = True
                    break
                else:
                    stack.pop()
            if not added:
                answerArr.append(-1)
        stack.append(arr[end])
    
    print(answerArr[::-1])


nearestSmallestRight([1, 4, 3, 0, 5, 2])






            
                    








