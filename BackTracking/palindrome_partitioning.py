import pdb
import copy
from typing import List
from pprint import pprint


class Solution1:

    def isPalindrome(self, ip):
        return ip == ip[::-1]

    def main(self, str_ip, ans_list):
        len_str = len(str_ip)

        for i in range(len_str):
            str_till_now = str_ip[:i+1]
            isPal = self.isPalindrome(str_till_now)
            if isPal:
                ans_list.append(str_till_now)
                if i+1 >= len_str:
                    self.solution.append(copy.deepcopy(ans_list))
                else:
                    self.main(str_ip[i+1:], ans_list)
                ans_list.pop()


    def partition(self, s: str) -> List[List[str]]:
        self.solution = []
        self.main(s, [])
        return self.solution

# a = Solution1().partition("a")
# print(a)


class Solution2:

    def main(self, str_ip, ans_list):
        if self.visited.get(str_ip):
            return        
        if self.solved:
            return
        len_str = len(str_ip)
        self.visited.update({str_ip: True})
        for i in range(len_str):
            str_till_now = str_ip[:i+1]
            presentInDict = str_till_now in self.wordDict
            if presentInDict:
                ans_list.append(str_till_now)
                if (i+1) >= len_str:
                    self.solution.append(copy.deepcopy(ans_list))
                    self.solved = True
                    return
                else:
                    self.main(str_ip[i+1:], ans_list)
                ans_list.pop()
        return

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.wordDict = wordDict
        self.solution = []
        self.solved = False
        self.visited = {}
        self.main(s, [])
        if self.solved:
            return True
        return False

# Solution2().wordBreak("catsandog", ["cats","dog","sand","and","cat"])


class Solution3:

    def main(self, str_ip, ans_list):

        len_str = len(str_ip)
        for i in range(len_str):
            str_till_now = str_ip[:i+1]
            presentInDict = str_till_now in self.wordDict
            if presentInDict:
                ans_list.append(str_till_now)
                if (i+1) >= len_str:
                    self.solution.append(" ".join(copy.deepcopy(ans_list)))
                else:
                    self.main(str_ip[i+1:], ans_list)
                ans_list.pop()
        return

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.wordDict = wordDict
        self.solution = []
        self.main(s, [])
        return self.solution

# a = Solution3().wordBreak("catsanddog", ["cat","cats","and","sand","dog"])
# print(a)



class Solution4:

    map1 = {
        2: ["a", "b", "c"],
        3: ["d", "e", "f"],
        4: ["g", "h", "i"],
        5: ["j", "k", "l"],
        6: ["m", "n", "o"],
        7: ["p", "q", "r", "s"],
        8: ["t", "u", "v"],
        9: ["w", "x", "y", "z"],
    }

    def main(self, digs, ansList):
        lenDigs = len(digs)
        if lenDigs==1:
            wordChoices = self.map1[int(digs[0])]
            for ch in wordChoices:
                ansList.append(ch)
                self.solution.append("".join(ansList))
                ansList.pop()
            return

        firstDig = int(digs[0])
        wordChoices2 = self.map1[firstDig]
        for ch in wordChoices2:
            ansList.append(ch)
            self.main(digs[1:], ansList)
            ansList.pop()
        
        return

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.solution = []
        self.main(digits, [])
        return self.solution


# a = Solution4().letterCombinations("23")



class Solution:

    def main(self, num: int):
        numStr = [i for i in str(num)]
        lenStr = len(numStr)
        for i in range(lenStr):
            for j in range(i, lenStr):
                temp_i = numStr[i]
                temp_j = numStr[j]
                numStr[j] = temp_i
                numStr[i] = temp_j
                numb = int("".join(numStr))
                if numb > self.solution:
                    self.solution = numb
                numStr[j] = temp_j
                numStr[i] = temp_i

    def maximumSwap(self, num: int) -> int:
        self.solution = float("-inf")
        self.main(num)
        return self.solution

a = Solution().maximumSwap(2736)
print(a)


        
        
