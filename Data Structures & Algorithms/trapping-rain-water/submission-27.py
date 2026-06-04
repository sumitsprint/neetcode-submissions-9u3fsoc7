class Solution:
    def trap(self, height: List[int]) -> int:
        w= 0
        n =len(height)
        l =0
        r =n-1
        l_m =height[l]
        r_m = height[r]

        while l < r:
            if height[l] < height[r]:
                l += 1
                l_m = max(l_m, height[l])
                w += l_m - height[l]
            else:
                r -= 1
                r_m = max(r_m, height[r])
                w += r_m - height[r]
        return w            



            


        