class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l = 0
        if not nums:
            return 0

        seen = set(nums)

        for n in nums:
            if n - 1 in seen:
                continue
            cs = 1
            fe = n + 1
            while fe in seen:
                cs += 1
                fe = fe + 1
            l = max(cs, l)
        return l        

            
        