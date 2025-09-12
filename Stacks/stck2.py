

arr = [1, 3, 0, 0, 1, 2, 4]

def fun1(arr):

    stack1 = []
    lenArr = len(arr)
    last_ele_index = lenArr-1

    answer = []

    for index in range(last_ele_index, -1, -1):
        is_stack_empty = not(bool(stack1))
        if is_stack_empty:
            answer.append("NA")
            stack1.append(arr[index])
            continue

        # stack is not empty
        curr_ele_of_arr = arr[index] 
        top_element_of_stack = stack1[-1]
        if top_element_of_stack > curr_ele_of_arr:
            answer.append(top_element_of_stack)
            stack1.append(curr_ele_of_arr)
        else:
            nearest_largest_to_right = "NA"
            while stack1:
                top_ele = stack1[-1]
                if top_ele > curr_ele_of_arr:
                    nearest_largest_to_right = top_ele
                    stack1.append(curr_ele_of_arr)
                    break
                else:
                    stack1.pop()
            answer.append(nearest_largest_to_right)

    print(answer[::-1])

def fun2(arr):
    stack1 = []
    lenArr = len(arr)
    answer = []

    for index in range(0, lenArr):
        is_stack_empty = not(bool(stack1))
        if is_stack_empty:
            answer.append("NA")
            stack1.append(arr[index])
            continue

        # stack is not empty
        curr_ele_of_arr = arr[index]
        top_element_of_stack = stack1[-1]

        if top_element_of_stack < curr_ele_of_arr:
            answer.append(top_element_of_stack)
            stack1.append(curr_ele_of_arr)
        else:
            nearest_smallest_to_left = "NA"
            while stack1:
                top_ele = stack1[-1]
                if top_ele < curr_ele_of_arr:
                    nearest_smallest_to_left = top_ele
                    stack1.append(curr_ele_of_arr)
                    break
                else:
                    stack1.pop()
            answer.append(nearest_smallest_to_left)

    print(answer)












fun2(arr)


