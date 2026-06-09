class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ls = 0
        n = len(nums)

        seen = set(nums)

        for n in nums:
            cs = 0
            if n - 1 not in seen:
                cs += 1
                fe = n + 1
                while fe in seen:
                    cs += 1
                    fe += 1
                ls = max(cs, ls)
        return ls            
                


        
        