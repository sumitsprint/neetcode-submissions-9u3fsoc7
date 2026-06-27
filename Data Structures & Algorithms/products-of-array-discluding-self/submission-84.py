class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mi = 1
        n = len(nums)
        prefix = []
        ans = [1 for _ in range(n)]

        for m in nums:

            prefix.append(mi)
            mi *= m

        mi = 1    

        for i in range(n-1,-1,-1):
            
            ans[i] = prefix[i] * mi
            mi *= nums[i]

        return ans       
        
        