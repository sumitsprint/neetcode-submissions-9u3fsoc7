class Solution:
    def maxArea(self, heights: List[int]) -> int:
        volm = 0
        for i in range(len(heights)-1):
            vol = 0
            for j in range(i+1,len(heights)):
                vol = min(heights[i], heights[j]) * (j - i)
                volm = max(volm, vol)
                
        return volm        

                

        