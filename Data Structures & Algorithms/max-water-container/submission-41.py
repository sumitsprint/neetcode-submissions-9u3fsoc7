class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        n = len(heights)
        right = n - 1
        max_a = 0

        while left < right:
            if heights[left] < heights[right]:
                w = right - left
                ht = heights[left]
                max_a = max(max_a, (ht *  w))
                left += 1

            else:
                w = right - left
                ht = heights[right]
                max_a = max(max_a, (ht *  w))
                right -= 1
        return max_a        


