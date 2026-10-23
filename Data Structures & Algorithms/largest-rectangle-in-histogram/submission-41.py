class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        n = len(heights)
        max_area = 0

        for i in range(len(heights)):
            bar = heights[i]
            while st and bar < heights[st[-1]]:
                ht = heights[st.pop()]
                right = i  # right boundary
                if st:
                    left = st[-1]
                else:
                    left = -1   
                w = right - left - 1
                max_area = max(max_area, (w * ht))


            st.append(i) 
        while st:
            ht = heights[st.pop()]
            right = n # right boundary
            if st:
                left = st[-1]
            else:
                left = -1   
            w = right - left - 1
            max_area = max(max_area, (w * ht))
        return max_area    


        