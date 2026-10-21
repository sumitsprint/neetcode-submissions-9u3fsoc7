class Solution:
    def trap(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1
        left_max = heights[0]
        right_max = heights[len(heights) - 1]
        w = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(heights[left], left_max)
                w += left_max - heights[left]

            else:
                right -= 1
                right_max = max(heights[right], right_max)
                w += right_max - heights[right]
        return w        













        

        