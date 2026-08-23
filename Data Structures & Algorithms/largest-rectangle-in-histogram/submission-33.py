class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        st = []
        m_a = 0

        for i in range(len(h)):
            while st and h[i] < h[st[-1]]:
                ht = h[st.pop()]
                left = st[-1] if st else -1
                right = i
                width = right - left - 1
                m_a = max(m_a, (ht*width))


            st.append(i)
        while st:
            ht = h[st.pop()]
            left = st[-1] if st else -1
            right = len(h)
            width = right - left - 1
            m_a = max(m_a, (ht*width))    

        return m_a    


        
        