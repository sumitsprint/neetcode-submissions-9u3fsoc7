class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        m = len(nums)
        prefix = [0 for _ in range(m)]
        ans = [1] * m

        mi = 1

        for i in range(m):
            prefix[i] = mi
            mi  *= nums[i]
        mi=1
        for i in range(m-1,-1,-1):
            ans[i] = prefix[i] *mi
            mi *= nums[i]
        return ans    




        