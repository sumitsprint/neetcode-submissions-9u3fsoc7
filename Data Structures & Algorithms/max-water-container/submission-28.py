class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0
        right = n - 1
        area = 0

        while left < right:
            ar = min(heights[left], heights[right]) * (right - left)
            area = max(ar, area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return area            
            
            
            



        
                




        