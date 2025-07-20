

def lcs(s1, s2, l1, l2):
    if l1<0 or l2<0:
        return 0
    
    if s1[l1]==s2[l2]:
        maxa = 1 + lcs(s1, s2, l1-1, l2-1)
    else:
        maxa = 0

    return max(
        maxa,
        lcs(s1, s2, l1-1, l2),
        lcs(s1, s2, l1, l2-1),
    )





def mainPrintLcs(s1, s2):
    prtAns = ""
    memo = {}

    def set_lcs(s1, s2, l1, l2, lcs_str):
        # non locals
        nonlocal prtAns
        nonlocal memo

        # memoization
        key = (l1, l2, lcs_str)
        if memo.get(key):
            return memo[key]

        # solve
        maxa = 0
        if l1<0 or l2<0:
            if len(lcs_str) > len(prtAns):
                prtAns = lcs_str
            maxa = 0
        else:
            if s1[l1]==s2[l2]:
                lcs_str1 = lcs_str + s1[l1]
                maxa = max(
                    1 + set_lcs(s1, s2, l1-1, l2-1, lcs_str1),
                    set_lcs(s1, s2, l1-1, l2, lcs_str),
                    set_lcs(s1, s2, l1, l2-1, lcs_str),
                )
            else:
                maxa = max(
                    set_lcs(s1, s2, l1-1, l2, lcs_str),
                    set_lcs(s1, s2, l1, l2-1, lcs_str),
                )
        
        # update memo
        memo[key] = maxa
        
        # ans
        return maxa
    
    # call nested function
    set_lcs(s1, s2, len(s1)-1, len(s2)-1, "")
    return prtAns[::-1]


s1 = "abcde"
s2 = "fgcdae"

# mainPrintLcsub(s1, s2)
ct1 = lcs(s1, s2, len(s1)-1, len(s2)-1)
print(ct1)
