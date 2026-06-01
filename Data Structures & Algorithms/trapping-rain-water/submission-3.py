class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = [0 for _ in range(n)]

        for i in range(1,n-1):
            left_max = max(height[:i])
            right_max = max(height[i+1:])
            ans[i] = max(0,min(left_max, right_max) - height[i])
        return sum(ans)    




        