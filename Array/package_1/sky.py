
# if bracket of type opening:
#     push to stack
# else:
#     # closing
#     top: opening = stack[top] optonal["(", None]
#     # ele present, top is None
        # return False


#     if top != :
#       return False
#     else:
#       pop it from stack
#       continue

# return True


dict1 = {"}": "{", ")": "(", "]": "["}
opening_brackets = ["(", "{", "["]

def fun1(ip):
    stack = []
    len1 = len(ip)

    for idx in range(len1):
        curr_char = ip[idx]
        if curr_char in opening_brackets:
            stack.append(curr_char)
        else:
            if not stack:
                return False
            top_char = stack[-1]
            top_char_expected = dict1[curr_char]
            if top_char != top_char_expected:
                return False
            else:
                stack.pop()

    if not stack:
        return True

    return False

ip = "({{{{"

valid = fun1(ip)
print(valid)





# Q2. Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
# The following rules define a valid string:
# * Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# * Any right parenthesis ')' must have a corresponding left parenthesis '('.
# * Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# * '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".


# Ex - (*) - valid
# Ex - *) - valid
# Ex - (* - valid
# Ex - )* - invalid

# "*(*))*"

# ")*"


# ""

# stck -> 

# if char is "(":
#     stck.push(char)
# elif char is ")":
#     # stack is empty -> return false
#     # top should be "(" or "*"
# else:
#     either
#         push to stack (opening)
#         copare top (closing one)
#         empty string ()
    





