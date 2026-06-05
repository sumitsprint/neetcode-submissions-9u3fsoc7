class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height) 
        l = 0
        r = n - 1
        l_m = height[l]
        r_m = height[r]
        w = 0

        while l < r:
            if l_m < r_m:
                l += 1
                l_m = max(height[l], l_m)
                w += l_m - height[l]
            else:
                r -= 1
                r_m = max(height[r], r_m)
                w += r_m - height[r]
        return w             
        