class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)    

            sq = 0
            while n > 0:
                di = n %10
                sq += di * di
                n = n//10
            n = sq    
        return True        




        