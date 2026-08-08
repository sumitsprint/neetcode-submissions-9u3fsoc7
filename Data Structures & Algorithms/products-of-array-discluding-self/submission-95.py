class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mi =1
        prefix = []

        n = len(nums)

        for i in range(n):
            prefix.append(mi)
            mi = mi * nums[i]

        ans = [1 for _ in range(n)]
        mi = 1

        for i in range(n-1, -1, -1):
            ans[i] = mi * prefix[i]
            mi = mi * nums[i] 

        return ans      


        