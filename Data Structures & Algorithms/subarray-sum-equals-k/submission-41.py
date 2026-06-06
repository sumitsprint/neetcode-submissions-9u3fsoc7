class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        fre = {0: 1}
        ans = 0
        prefix = 0

        for n in nums:
            prefix += n
            if prefix - k in fre:
                ans += fre.get(prefix - k, 0)
                # fre[prefix] = fre.get(prefix,0) + 1
            fre[prefix] = fre.get(prefix,0) + 1
        return ans        
                
        


        