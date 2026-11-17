class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        fre = {0:1}
        prefix = 0
        s = 0

        for n in nums:
            prefix += n
            pre = prefix - k
            if pre in fre:
                s += fre.get(pre)
            fre[prefix] = fre.get(prefix, 0) + 1
        return s         

        