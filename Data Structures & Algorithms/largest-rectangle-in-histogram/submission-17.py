class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        max_a = 0

        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                height = heights[stack.pop()]
                if stack:
                    left = stack[-1] 
                else:
                    left = -1 
                right = i    
                width = right - left - 1

                area = width * height
                max_a = max(area, max_a)          
            stack.append(i)

        while stack:
            height = heights[stack.pop()]
            if stack:
                left = stack[-1] 
            else:
                left = -1 
            right = n    
            width = right - left - 1

            area = width * height
            max_a = max(area, max_a)  
        return max_a    

        
        