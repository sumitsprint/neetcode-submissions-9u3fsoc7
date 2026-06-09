class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = [1] * len(nums)
        ans = []
        
        # 1. Calculate Prefixes
        mi = 1
        for i in range(len(nums)):
            prefix.append(mi)
            #preparing state for next iteration  -- important
            mi = mi * nums[i]

        # FIX: Reset mi to 1 before calculating Suffixes
        mi = 1 
        for i in range(len(nums) - 1, -1, -1):
            suffix[i] = mi
            #preparing state for next iteration  -- important
            mi = mi * nums[i]    

        # 3. Combine them
        for i in range(len(nums)):
            ans.append((prefix[i] * suffix[i]))
        return ans