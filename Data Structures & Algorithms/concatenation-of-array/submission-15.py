class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans

        # T.C- O(n)
# S.C - O(n)           
"""Time Complexity (TC): 
𝑂
(
𝑛
)
 — the nested loops run exactly 
2
𝑛
 iterations, which simplifies to linear time.

Space Complexity (SC): 
𝑂
(
𝑛
)
 — the output list ans stores 
2
𝑛
 elements, proportional to the input size."""