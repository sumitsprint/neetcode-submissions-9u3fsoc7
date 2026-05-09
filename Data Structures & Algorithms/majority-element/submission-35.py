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

        # boyre moore voting algo
        # tc - O(n)
        # sc- O(1)
        # only works for n/2
        # different element cancel each other out 
        # if a true majority exists it survives all cancelations