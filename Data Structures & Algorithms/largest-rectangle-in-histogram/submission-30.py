class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        n = len(heights)
        max_area = 0

        for i in range(n):
            bar = heights[i]

            # shorter bar resolves waiting bars
            while st and bar < heights[st[-1]]:
                ht = heights[st.pop()]

                # new top = left boundary
                if st:
                    left = st[-1]
                else:
                    left = -1

                # current bar = right boundary
                right = i

                width = right - left - 1
                a = width * ht
                max_area = max(a, max_area)

            # bar waits for a shorter bar
            st.append(i)

        # bars still waiting at the end
        while st:
            ht = heights[st.pop()]

            # new top = left boundary
            if st:
                left = st[-1]
            else:
                left = -1

            # end of array = right boundary
            right = n

            width = right - left - 1
            a = width * ht
            max_area = max(a, max_area)

        return max_area