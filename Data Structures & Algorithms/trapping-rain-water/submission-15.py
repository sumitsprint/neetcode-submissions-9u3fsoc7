class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        
        left = 0
        right = n - 1

        for i in range(1,n-1):
            left_max = max(height[:i])
            right_max = max(height[i+1:])
            
            water = min(left_max, right_max) - height[i]
            res += max(0, water)

                
                

        return res 

        
        