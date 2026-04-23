class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        currentCandidate , count = 0, 0
        for n in nums:
            if count == 0:
                currentCandidate = n
            if n == currentCandidate:
                count = count + 1
            else:
                count = count - 1
        return currentCandidate            

        