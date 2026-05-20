class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        if not nums:
            return 0

        lon = 0

        for n in nums:
            if n - 1 in seen:
                continue
            cs = 1
            fe  = n + 1
            while fe in seen:
                cs += 1
                fe += 1
            lon = max(lon, cs)
        return lon                
        