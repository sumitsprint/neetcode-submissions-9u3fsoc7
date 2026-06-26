class Solution:
    def isHappy(self, n: int) -> bool:
        see = set()
        
        while n != 1:
            if n in see:
                return False
            see.add(n)    

            dsq = 0

            while n > 0:
                d = n % 10
                dsq += d*d
                n = n // 10

            n = dsq  
        return True      


        