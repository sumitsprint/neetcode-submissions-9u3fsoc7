class Solution:
    def trap(self, height: List[int]) -> int:
        w = 0
        for i in range(1,len(height)-1):
            w += max(0,min(max(height[:i]), max(height[i+1:])) - height[i])
        return w    
            


        