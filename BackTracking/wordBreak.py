# https://leetcode.com/problems/word-break/description/


class Solution(object):

    def main(self, wordDict, wrd):
        dict1 = {}

        def fun1(start, end):
            if (start, end) in dict1:
                return dict1[(start, end)]
            else:
                for i in range(start, end+1):
                    wrd1 = wrd[start:i+1]
                    wrd2 = wrd[i+1:]

                    if wrd1 in wordDict:
                        if not wrd2:
                            dict1[(start, end)] = True
                            return True
                        elif len(wrd2) == 1:
                            if wrd[end] in wordDict:
                                dict1[(start, end)] = True
                                return True
                        else:
                            remaining_pos = fun1(i+1, end)
                            if remaining_pos:
                                dict1[(start, end)] = True
                                return True
                            else:
                                continue
                dict1[(start, end)] = False
                return False

        return fun1(0, len(wrd)-1)

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        return self.main(wordDict, s)

wordDict = ["apple","pen", "e"]
wrd = "applepenapplee"

c1 = Solution().wordBreak(wrd, wordDict)
print(c1)


