class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Frequency of characters inside the current window [left, right]
        fre = [0] * 26

        left = 0

        # Highest frequency of any character seen in the current window
        max_freq = 0

        # Length of the longest valid window found so far
        max_length = 0

        for right in range(len(s)):

            # Expand the window by including s[right]
            fre[ord(s[right]) - ord('A')] += 1

            # Update the frequency of the dominant character
            max_freq = max(max_freq, fre[ord(s[right]) - ord('A')])

            # Current window length
            window_length = right - left + 1

            # Number of replacements needed to make the entire
            # window consist of the dominant character
            validity = window_length - max_freq

            # If more than k replacements are required,
            # shrink the window from the left until it becomes valid
            while validity > k and left < len(s):

                # Remove the leftmost character from the window
                fre[ord(s[left]) - ord('A')] -= 1

                # Move the left boundary rightward
                left += 1

                # Recompute the window length after shrinking
                window_length = right - left + 1

                # Recompute the replacements needed
                validity = window_length - max_freq

            # At this point the window is valid,
            # so record its length if it is the largest seen so far
            max_length = max(window_length, max_length)

        return max_length