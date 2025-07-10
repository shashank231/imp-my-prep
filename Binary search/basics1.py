# pre-placed
# What is the pattern of the binary search algorithm based DSA question?
# - Whenever we see a sorted array or a sorted matrix, we can think of binary search.
# - Whenever we see a question that asks for the first or last occurrence of an element, we can think of binary search.
# - Whenever we see a question that asks for the smallest or largest element in a range, we can think of binary search.
# - Whenever we see a question that asks for the number of occurrences of an element, we can think of binary search.
# - Whenever we have questions like up to a certain point the answers are possible and after a certain point answer is not possible 
# we can always apply binary search in such cases

# Binary search on answers
# - Whenever you don't know how to approach but it seems like if you assume an answer, then you can surely
# check that if that no. is answer or not
# Essentially you dont know how to get answer.. but you can write a fn to check if a particular no. is answer or not.. plus
# you can negate the left or right side of answer depending upon whether the answer was possible or not..
# In such cases we can use Binary search by slowly approaching answer

# Min of Max
# Max of Min


# GPT
# - Show me some important and interesting binary search problems, that initially doesn't look like binary search problems.

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2  # Calculate the middle index: avoid integer overflow in some languages
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# TODO: work on improved version of binary search algorithm using recursion.
def binary_search_rec(arr, target):
    len_arr = len(arr)
    if len_arr == 1:
        if arr[0] == target:
            return 0
        else:
            return -1

    left = 0
    right = len_arr - 1
    mid = (left + right) // 2
    left_arr = arr[:mid+1]
    right_arr = arr[mid+1:]

    i_left = -1
    i_right = -1
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        i_right = binary_search_rec(right_arr, target)
    else:
        i_left = binary_search_rec(left_arr, target)

    if i_left != -1:
        return i_left
    elif i_right != -1:
        return mid + i_right + 1 
    else:
        return -1

# sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# target_value = 19
# r1 = binary_search(sorted_array, target_value)
# r2 = binary_search_rec(sorted_array, target_value)
# print(f"Binary search result 1: {r1}")
# print(f"Binary search result 2: {r2}")


# -------------------------------------------------------------------------------------------------
# lower bound: smallest index such that arr[i] >= target
# Why is it called "lower bound"?
    # Think of the array as a set of numbers arranged in order.
    # For a given target, we are asking:
        # "Where is the smallest number that is still big enough?"
def lower_bound(arr, target):
    len_arr = len(arr)
    left = 0
    right = len_arr - 1

    ans = len_arr   # consider this as ans for now!!

    while (left <= right):
        mid = (left + right)//2
        if arr[mid] >= target:
            ans = mid      # maybe an answer
            right = mid-1  # look for more small index on left
        else:  
            left = mid+1   # look for right

    return ans


# -------------------------------------------------------------------------------------------------
# upper bound: smallest index such that arr[i] > target
# Why is it called "upper bound"?
    # In arrays, the upper bound gives you the point right above the target.

def upper_bound(arr, target):
    len_arr = len(arr)
    left = 0
    right = len_arr - 1

    ans = len_arr  # consider this as ans for now!!

    while (left <= right):
        mid = (left + right)//2
        if arr[mid] > target:
            ans = mid      # maybe an answer
            right = mid-1  # look for more small index on left
        else:  
            left = mid+1   # look for right

    return ans


# -------------------------------------------------------------------------------------------------
# Search insert position
# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

# => Think for a second and you will realize its same as finding a lower bound :)
# Or I also did it like this

def searchInsert(arr, target):
    len_arr = len(arr)
    left = 0
    right = len_arr - 1

    ans = 0
    while (left <= right):
        mid = (left + right)//2
        if arr[mid] == target:
            ans = mid
            return ans
        elif arr[mid] < target:
            ans = mid+1
            left = mid+1 
        else:
            ans = mid 
            right = mid-1
    return ans


# -------------------------------------------------------------------------------------------------
# Floor and ceil in sorted array
# Floor: larget no in array <= x
# Ceil: smallest no in array >= x => lower bound

def floorArr(arr, target):
    len_arr = len(arr)
    left = 0
    right = len(arr)-1
    ans_index = -1

    while(left <= right):
        mid = (left + right)//2 
        if arr[mid] <= target:
            ans = mid
            left = mid+1
        else:
            right = mid-1
    
    return arr[ans_index]

