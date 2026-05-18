class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = [1] * len(nums)
        ans = []
        mi = 1
        bm = 1
        
        for i in range(len(nums)):
            prefix.append(mi)
            mi = mi * nums[i]

        for i in range(len(nums) - 1, -1, -1):
            suffix[i] = bm
            bm = bm * nums[i]    

        for i in range(len(nums)):
            ans.append((prefix[i] * suffix[i]))
        return ans        

        