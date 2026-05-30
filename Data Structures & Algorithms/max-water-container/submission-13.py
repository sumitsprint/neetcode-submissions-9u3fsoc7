class Solution:
    def maxArea(self, heights: List[int]) -> int:
        voli = 0
        for i in range(len(heights)-1):
            vol = 0
            for j in range(i+1,len(heights)):
                vol = min(heights[i], heights[j]) * (j - i)
                voli = max(voli, vol)
                
        return voli        

                

        