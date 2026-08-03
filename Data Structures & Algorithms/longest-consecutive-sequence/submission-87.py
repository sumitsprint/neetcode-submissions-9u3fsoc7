class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ls = 0
        see = set(nums)
        # cs = 0
        

        for n in see:
            cs = 0
            if n - 1 not in see:
                cs += 1
                fe = n+1

                while fe in see:
                    cs += 1
                    fe += 1
                ls = max(ls,cs)
        return ls            



        