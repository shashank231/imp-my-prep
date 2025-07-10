class Solution:
    t11 = "("
    t12 = ")"
    t21 = "["
    t22 = "]"
    t31 = "{"
    t32 = "}"
    
    def isValid(self, s: str) -> bool:
        c1 = 0
        c2 = 0
        c3 = 0
        solution = True
        for i in s:
            if i in (self.t11, self.t12):
                if i==self.t11:
                    c1 += 1
                else:
                    c1 -= 1
                if c1 < 0:
                    solution=False
                    break
            elif i in (self.t21, self.t22):
                if i==self.t21:
                    c2 += 1
                else:
                    c2 -= 1
                if c2 < 0:
                    solution=False
                    break
            elif i in (self.t31, self.t32):
                if i==self.t31:
                    c3 += 1
                else:
                    c3 -= 1
                if c3 < 0:
                    solution=False
                    break
        if c1 != 0 or c2 != 0 or c3 != 0:
            return False
        return solution
            
            




        