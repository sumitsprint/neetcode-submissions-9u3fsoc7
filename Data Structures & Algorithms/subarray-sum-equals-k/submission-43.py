class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        fre = {0:1}
        prefix = 0
        ans = 0
        for i in range(len(nums)):
            prefix = prefix + nums[i]
            if prefix - k in fre:
                ans+= fre.get(prefix - k, 0)
            fre[prefix] = fre.get(prefix, 0) +1    
        return ans    









        