class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        h2 = 0

        leftm= height[left]
        rightm = height[right]

        while left < right:
            if leftm < rightm:
                left += 1
                leftm = max(leftm, height[left])
                h2 += leftm-height[left]
            else:
                right -= 1
                rightm = max(rightm, height[right])
                h2 += rightm-height[right] 
        return h2          
                
            
            
        