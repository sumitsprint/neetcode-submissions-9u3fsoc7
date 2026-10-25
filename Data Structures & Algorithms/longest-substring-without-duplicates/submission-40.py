class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        see = set()
        left  = 0
        m_l = 0
        
        for right in range(len(s)):
            c = s[right]
            while c in see:
                see.remove(s[left])
                left += 1

            see.add(c)
            length = right - left + 1


            m_l = max(m_l, length)
        return m_l    


        