class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        seen = set(nums)
        longest_streak = 0

        for n in nums:
            pre = n - 1
            if pre in seen:
                continue
            cs = 1  
            fe = n + 1
            while fe in seen:
                cs += 1
                
                
                fe += 1
            longest_streak = max(longest_streak, cs)    
                
        return longest_streak         
                


        