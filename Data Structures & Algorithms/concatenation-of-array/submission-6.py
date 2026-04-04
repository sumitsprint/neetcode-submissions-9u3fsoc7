class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(0,2,1):
            for n in nums:
                ans.append(n)

        return ans        