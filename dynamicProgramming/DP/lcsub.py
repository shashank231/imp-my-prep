
max_len = 0

def lcs_sub(s1, s2, l1, l2, count):
    if l1 < 0 or l2 < 0:
        return count

    if s1[l1] == s2[l2]:
        count = lcs_sub(s1, s2, l1 - 1, l2 - 1, count + 1)
    
    return max(
        count,
        lcs_sub(s1, s2, l1 - 1, l2, 0),
        lcs_sub(s1, s2, l1, l2 - 1, 0)
    )

def mainPrintLcsSub(s1, s2):
    prtAns = ""

    def lcs_sub(s1, s2, l1, l2, count, ans):
        nonlocal prtAns
        if l1 < 0 or l2 < 0:
            return count

        if s1[l1] == s2[l2]:
            ans1 = ans + s1[l1]
            if len(ans1) > len(prtAns):
                prtAns = ans1
            count = lcs_sub(s1, s2, l1 - 1, l2 - 1, count + 1, ans1)
        
        return max(
            count,
            lcs_sub(s1, s2, l1 - 1, l2, 0, ""),
            lcs_sub(s1, s2, l1, l2 - 1, 0, ""),
        )
    
    lcs_sub(s1, s2, len(s1)-1, len(s2)-1, 0, "")
    print(prtAns[::-1])

s1 = "abcdefgrt"
s2 = "fgcdaebcdert"

# mainPrintLcsub(s1, s2)
ct1 = lcs_sub(s1, s2, len(s1)-1, len(s2)-1, 0)
print(ct1)

mainPrintLcsSub(s1, s2)