class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        ans =0 
        fre = {0:1}
        current_prefix = 0

        for n in nums:
            current_prefix += n
            prev = current_prefix - k
            if prev in fre:
                ans += fre.get(prev,0)
            fre[current_prefix] = fre.get(current_prefix,0 ) +1
        return ans      
                
        