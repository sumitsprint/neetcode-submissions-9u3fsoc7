class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n - 1
        a = 0
        
        while l < r:
            if height[l] < height[r]:
                ta = height[l] * (r -l)
                a = max(a,ta)
                l += 1
            else:
                ta = height[r] * (r -l)
                a = max(a,ta)
                r -= 1
        return a
        