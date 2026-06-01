class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = [0 for _ in range(n)]
        
        left = 0
        right = n - 1

        for i in range(1,n-1):
            
            water = min(max(height[:i]), max(height[i+1:])) - height[i]
            res[i] = max(0, water)

                
                

        return sum(res) 

        
        