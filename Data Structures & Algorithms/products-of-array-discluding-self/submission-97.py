class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        mi = 1
        prefix = [1 for _ in range(len(nums))]

        for i in range(len(nums)):
            prefix[i] = mi
            mi = mi * nums[i]

        mi = 1
        ans = [1 for _ in range(len(nums))]

        for i in range(len(nums)-1, -1, -1):
            ans[i] = prefix[i] * mi
            mi = mi * nums[i]
        return ans    




        