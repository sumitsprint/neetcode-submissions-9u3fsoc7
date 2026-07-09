class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        max_area = 0

        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                height = heights[stack.pop()]
                if stack:
                    left = stack[-1]
                else:
                    left = -1
                right = i    
                width = right -left -1
                area = width * height
                max_area = max(max_area, area)        
            stack.append(i)   
        while stack:

            height = heights[stack.pop()]

            if stack:
                left = stack[-1]
            else:
                left = -1
    
            right = n

            width = right - left - 1

            area = height * width
            max_area = max(max_area, area)     
                
        return max_area    
            



        