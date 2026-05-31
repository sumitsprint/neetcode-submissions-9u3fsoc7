class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        area_max = 0


        for i in range(n - 1):
            area = 0
            for j in range(n):
                area = min(heights[i], heights[j])* (j-i)
                area_max = max(area_max, area)
        return area_max        

        