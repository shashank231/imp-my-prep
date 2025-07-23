# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:        
        start = 0
        lenS = len(s)
        solution = 0

        if lenS >= 1:
            map = {s[0]: 1}
        else:
            map = {}

        for end in range(1, lenS):
            word = s[end]
            if not map.get(word):
                map[word] = 1
            else:
                solution = max(solution, end-start)
                
                while s[start] != word:
                    map[s[start]] -= 1
                    start += 1

                start += 1

        solution = max(solution, len(s) - start)
        return solution