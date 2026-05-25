class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        seen =  set(nums)
        s = 0
        # cs = 0
        for n in nums:
            if n -1 in seen:
                continue
            c = 1
            fe = n + 1
            while fe in seen:
                c += 1
                fe += 1
            s = max(c,s)
        return s                
        