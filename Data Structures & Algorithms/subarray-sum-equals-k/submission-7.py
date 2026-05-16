class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        fre = {0:1}
        pre = 0
        ans = 0
        for n in nums:
            pre += n
            need = pre - k
            if need in fre:
                ans += fre[need]

            fre[pre] = fre.get(pre , 0) + 1
        return ans        
            



        
        