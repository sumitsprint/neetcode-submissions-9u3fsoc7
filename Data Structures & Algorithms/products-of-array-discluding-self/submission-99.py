class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        ans = [1] * len(nums)
        mi = 1


        for i in range(len(nums)):
            prefix.append(mi)
            mi = mi * nums[i]

        mi = 1

        for i in range(len(nums)-1,-1,-1):
            ans[i] = mi*prefix[i]
            mi = mi * nums[i]
        return ans    
            


            



        