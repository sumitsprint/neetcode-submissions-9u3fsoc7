class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ls = 0
        see = set(nums)

        for n in see:
            if n-1 not in see:
                cs = 1
                fe = n + 1
                while fe in see:
                    cs += 1
                    fe += 1
                ls = max(ls, cs)
        return ls        
        