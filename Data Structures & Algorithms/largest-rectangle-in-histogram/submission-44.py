class Solution:
    def largestRectangleArea(self, height: List[int]) -> int:
        st = []
        max_a = 0
        n = len(height)

        for i in range(len(height)):
            while st and height[i] < height[st[-1]]:
                ht = height[st.pop()]
                if st:
                    left = st[-1]
                else:
                    left = -1    
                right = i
                width = right - left - 1
                a = width * ht
                max_a = max(max_a, a)


            st.append(i)
        while st:
            ht = height[st.pop()]
            if st:
                left = st[-1]
            else:
                left = -1    
            right = n
            width = right - left - 1
            a = width * ht
            max_a = max(max_a, a)


        return max_a
            
            
             
            

        