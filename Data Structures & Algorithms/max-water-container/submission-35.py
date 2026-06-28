class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        n = len(heights)
        right = n - 1
        max_a = 0



        while left < right:
            if heights[left] < heights[right]:
                area = heights[left] * (abs(right-left))
                max_a = max(area , max_a)
                left += 1

            else:
                area = heights[right] * (abs(right-left))
                max_a = max(area , max_a)
                right -= 1
        return max_a        