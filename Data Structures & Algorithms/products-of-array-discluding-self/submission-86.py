class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        m = len(nums)
        prefix = []
        mi = 1
        ans = [1 for _ in range(m)]


        for n in nums:
            prefix.append(mi)
            mi *= n

        mi = 1

        for i in range(m - 1, -1, -1):
            ans[i] = mi * prefix[i]
            mi *= nums[i]

        return ans    



            

        
        