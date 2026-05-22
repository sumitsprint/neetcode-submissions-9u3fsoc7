class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        current = None

        for n in nums:
            if count == 0:
                current = n
            if n == current:
                count += 1
            else:
                count -= 1
        return current                
        