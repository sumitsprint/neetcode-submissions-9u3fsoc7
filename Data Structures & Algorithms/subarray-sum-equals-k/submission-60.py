class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        map1 = {0:1}
        ans = 0
        cp =0 

        for n in nums:
            cp += n
            pp = cp - k
            if pp in map1:
                ans += map1.get(pp, 0)
            map1[cp] = map1.get(cp , 0) +1
        return ans       

        