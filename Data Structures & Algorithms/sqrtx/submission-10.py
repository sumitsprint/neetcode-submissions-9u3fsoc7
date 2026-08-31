class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right =  x

        while left <= right:
            mid = (left + right) // 2

            if (mid * mid) > x:
                right = mid - 1

            else:
                left = mid + 1 #left moves whenever it is valid 

        return left - 1   


        
         
                


        