class Solution:
    def isHappy(self, n: int) -> bool:
        see = set()

        while n != 1:
            if n in see:
                return False
            see.add(n)

        

            ds = 0
            while n > 0:
                res = n % 10
                ds += res * res
                n = n // 10

            n = ds  
        return True      









            
        
                
                