class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        see = set(nums)

        m_s = 0
        # c_s = 0
        for s in see:
            c_s = 0
            
            
            if s-1 not in see:
                c_s = 1
                f_e = s +1
                while f_e in see:
                    c_s += 1
                    f_e += 1
                m_s = max(m_s, c_s)
        return m_s            


        
        