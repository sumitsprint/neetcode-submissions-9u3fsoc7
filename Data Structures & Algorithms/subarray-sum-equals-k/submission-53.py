class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        fre = {0:1}
        prefix = 0
        for n in nums:
            prefix += n
            need = prefix - k
            if need in fre:
                ans  += fre.get(need)
            fre[prefix] = fre.get(prefix, 0)+1
        return ans         
        