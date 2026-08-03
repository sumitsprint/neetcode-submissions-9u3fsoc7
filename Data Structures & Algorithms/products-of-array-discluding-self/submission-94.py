class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mi  = 1
        n = len(nums)

        prefix = []

        for m in nums:
            prefix.append(mi)
            # preparing state for next iteration
            mi *= m

        ans = [1 for _ in range(n)]
        mi = 1
        for i in range(n-1,-1,-1):
            ans[i] = mi * prefix[i]
            mi *= nums[i] 
        return ans    
        