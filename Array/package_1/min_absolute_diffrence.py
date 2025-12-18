
import copy

class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr1 = sorted(arr)
        min_abs_diff = float("inf")
        for i in range(1, len(arr1)):
            diff = arr1[i]-arr1[i-1]
            if diff < min_abs_diff:
                min_abs_diff = diff

        lenArr = len(arr)
        frmt = lambda nums: (min(nums), max(nums))
        frmtop = lambda nums: [min(nums), max(nums)]
        output = list()
        set_mem = set()

        def fillOutput(ans, start):
            lenAns = len(ans)
            if lenAns == 2:
                frmt_ans = frmt(ans)
                if frmt_ans in set_mem:
                    return
                set_mem.add(frmt_ans)
                abs_diff = abs(ans[0]-ans[1])
                if abs_diff == min_abs_diff:
                    output.append(frmtop(ans))
            elif lenAns < 2 and start < lenArr:
                newAns1 = ans + [arr[start]]
                newAns2 = ans
                fillOutput(newAns1, start+1)
                fillOutput(newAns2, start+1)
            else:
                return

        fillOutput([], 0)
        return output



a = Solution().minimumAbsDifference([3,8,-10,23,19,-4,-14,27])

print(a)