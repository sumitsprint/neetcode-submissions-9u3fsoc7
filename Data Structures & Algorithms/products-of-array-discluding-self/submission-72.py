class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        m = len(nums)
        mi = 1
        prefix = []
        ans = [1] * m

        for n in nums:
            prefix.append(mi)
            mi *= n # preparing state for next iteration

        mi = 1
        for i in range(m-1,-1,-1):

            ans[i] =  prefix[i] * mi
            mi = mi * nums[i]
        return ans






        