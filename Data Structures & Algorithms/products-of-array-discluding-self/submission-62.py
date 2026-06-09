class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        ans = [1] * n

        mi = 1

        for i in range(n):
            prefix[i] = mi
            mi *= nums[i]

        mi = 1
        for i in range(n - 1, -1, -1):
            suffix[i] = mi
            mi *= nums[i]

        for i in range(n):
            ans[i] = suffix[i] * prefix[i]

        return ans    


        
        