class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 0 
        right = n - 1
        left_m = height[left]
        right_m = height[right]
        water = 0

        while left < right:
            if left_m < right_m:
                left += 1
                left_m = max(left_m, height[left])
                water += left_m - height[left]

            else:
                right -=1
                right_m = max(right_m, height[right])
                water += right_m - height[right]

        return water            

         
        
        