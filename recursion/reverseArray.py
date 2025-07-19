
def fun1(arr):
    if len(arr) <= 1:
        return arr
    rev_Arr = fun1(arr[1:]) + [arr[0]]
    return rev_Arr



def fun2(n, k):
    def helper(n):
        if n==1:
            return "0"        
        prevStr = helper(n-1)
        ansStr = ""
        for i in prevStr:
            if i=="0":
                ansStr += "01"
            else:
                ansStr += "10"
        return ansStr
    
    ms = helper(n)
    return ms[k-1]

fun2(3, 1)