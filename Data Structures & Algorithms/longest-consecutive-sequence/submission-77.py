class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if not nums:
            # return 0

        longest_streak = 0
        seen = set(nums)

        for n in nums:
            if n - 1 in seen:
                continue
            current_streak = 1    
            forward_element = n + 1
            while forward_element in seen:
                current_streak += 1
                forward_element += 1
            longest_streak = max(longest_streak, current_streak)
        return longest_streak       


        