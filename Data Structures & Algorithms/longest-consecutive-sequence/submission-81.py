class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        seen = set(nums)  # Removes duplicates and allows O(1) lookups

        # CRITICAL FIX: Iterate over 'seen' instead of 'nums'
        for n in seen:
            # Only start checking if 'n' is the absolute start of a sequence
            if n - 1 in seen:
                continue
                
            current_streak = 1    
            forward_element = n + 1
            
            while forward_element in seen:
                current_streak += 1
                forward_element += 1
                
            longest_streak = max(longest_streak, current_streak)
            
        return longest_streak       


        #By simply changing for n in nums: to for n in seen:, 
        #you instantly eliminate all duplicate processing.