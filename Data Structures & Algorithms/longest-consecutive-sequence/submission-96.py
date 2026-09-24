class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        see = set(nums)
        max_c = 0
        for n in see:
            if n-1 not in see:
                cs = 1
                fe = n +1
                while fe in see:
                    cs += 1
                    
                    fe += 1
                max_c = max(max_c, cs)    
        return max_c                


        