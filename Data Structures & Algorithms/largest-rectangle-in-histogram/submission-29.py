class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        n = len(heights)
        max_area = 0

        for i in range(n):
            bar = heights[i]
            while st and bar < heights[st[-1]] :
                ht = heights[st.pop()]
                if st:
                    left = st[-1]
                else:
                    left = -1
                right = i    

                width =   right - left - 1
                a = width * ht
                max_area = max(a, max_area)

            st.append(i)

        while st:
            ht = heights[st.pop()]
            if st:
                left = st[-1]
            else:
                left = -1
            right = n  

            width =   right - left - 1
            a = width * ht
            max_area = max(a, max_area)

        
            


            
        return max_area
        