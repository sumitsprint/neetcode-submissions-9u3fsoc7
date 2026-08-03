class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        fre =  {0:1}
        pre =  0
        ans  = 0
        

        for n in nums:
            pre += n
            if pre -k in fre:
                ans += fre.get(pre-k)
            fre[pre] = fre.get(pre, 0) + 1    
        return ans        

        