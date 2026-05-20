class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        map1 = {0:1}
        prefix = 0

        for n in nums:
            prefix += n
            need = prefix - k
            if need in map1:
                ans += map1.get(need, 0)
            map1[prefix] = map1.get(prefix, 0) + 1
        return ans        

            
        