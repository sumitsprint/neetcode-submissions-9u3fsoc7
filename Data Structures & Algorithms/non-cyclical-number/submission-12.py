class Solution:
    def isHappy(self, n: int) -> bool:
        see = set()
        
        while n != 1:
            if n in see:
                return False
            see.add(n)
            digit_s = 0

            
            
            while n > 0:

                d_s = n % 10
                

                digit_s += d_s * d_s
                n = n // 10
            n = digit_s
        return True        


        