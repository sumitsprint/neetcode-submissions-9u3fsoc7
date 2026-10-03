class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        st = []
        max_a = 0

        for i in range(n):
            while st and heights[i] < heights[st[-1]]:
                ht = heights[st.pop()]
                right = i
                if st:
                    left = st[-1]
                else:
                    left = -1

                width = right - left - 1
                a = width * ht
                max_a = max(max_a, a)


            st.append(i)

        while st:
            ht =  heights[st.pop()]
            if st:
                left = st[-1]

            else:
                left = - 1

            right = n
            width = right - left - 1
            a = width * ht
            max_a = max(max_a, a)        
        return max_a      




        