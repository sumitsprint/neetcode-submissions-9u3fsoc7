class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_l = 0
        fre = {}

        left = 0
        m_f = 0

        for right in range(len(s)):
            c = s[right]

            fre[c] = fre.get(c, 0) + 1

            w_l = right - left  + 1

            m_f = max(m_f, fre[c])

            valid = w_l - m_f

            while valid > k:
                fre[s[left]] -= 1
                left += 1

                w_l = right - left + 1
                
                valid = w_l - m_f

            max_l = max(max_l, w_l)
        return max_l        


        