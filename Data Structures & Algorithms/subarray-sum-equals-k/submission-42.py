class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        map1 = {0:1}
        prefix = 0
        ans = 0
        for n in nums:
            prefix += n
            pp = prefix - k
            if pp in map1:
                ans += map1.get(pp, 0)
            map1[prefix] = map1.get(prefix, 0) + 1
        return ans        


        