class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0
        right = n - 1
        max_a = 0

        while left < right:
            ht = min(heights[left], heights[right])
            area  = ht * (right - left)
            max_a = max(area, max_a)
            if heights[left] < heights[right]:
                left += 1

            else:
                right -= 1
        return max_a            



        