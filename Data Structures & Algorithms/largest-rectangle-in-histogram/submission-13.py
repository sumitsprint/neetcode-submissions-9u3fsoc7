class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        max_a = 0

        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                height = heights[stack.pop()]
                right = i
                if stack:
                    
                    left = stack[-1]
                else:
                    left = -1
                width = right - left - 1
                area = width * height    
                max_a = max(max_a, area)  
            stack.append(i)

        while stack:
            height = heights[stack.pop()]
            right = n
            if stack:
                left = stack[-1]
            else:
                left = -1
            width = right - left - 1
            area = width * height    
            max_a = max(max_a, area)          
                
        
            
        return max_a

            



        