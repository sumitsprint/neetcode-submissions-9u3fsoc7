class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mi = 1
        ans = [1] * len(nums)
        p = []

        for i in range(len(nums)):
            p.append(mi)
            mi = mi * nums[i]

        mi = 1

        for i in range(len(nums) - 1, -1, -1):
            ans[i] = mi * p[i]
            mi = mi * nums[i]

        return ans        
