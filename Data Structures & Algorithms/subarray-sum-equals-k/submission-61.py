class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre = {0: 1}
        prefix = 0
        s = 0
        for n in nums:
            prefix += n
            pre_p = prefix - k

            if pre_p in pre:
                s += pre.get(pre_p)
            pre[prefix] = pre.get(prefix, 0) + 1
        return s    


        