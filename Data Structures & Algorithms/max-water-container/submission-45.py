class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_a = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            if heights[left] < heights[right]:
                w = right - left
                max_a = max(max_a, (w * heights[left]))
                left += 1

            else:
                w = right - left
                max_a = max(max_a, (w * heights[right]))
                right -= 1
        return max_a        



