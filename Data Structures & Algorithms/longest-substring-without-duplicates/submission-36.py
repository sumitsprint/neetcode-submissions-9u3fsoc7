class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_l = 0
        left = 0
        see = set()

        for right in range(len(s)):
            while s[right] in see:
                see.remove(s[left])
                left += 1
            max_l = max(max_l, right-left +  1  )

            see.add(s[right])
        return max_l    





        