class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        left_max = height[left]
        right_max = height[right]
        w = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(height[left] , left_max)
                w += left_max - height[left]
            else:
                right -= 1
                right_max = max(height[right] , right_max)
                w += right_max - height[right]
        return w        

        