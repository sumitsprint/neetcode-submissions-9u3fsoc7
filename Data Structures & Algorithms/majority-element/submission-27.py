class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        currentCandidate = 0
        count = 0
        for n in nums:
            if count == 0:
                currentCandidate = n
            if n == currentCandidate:
                count += 1
            else:
                count -= 1
        return currentCandidate                
        