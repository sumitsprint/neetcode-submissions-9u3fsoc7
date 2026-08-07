class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        can = None

        for n in nums:
            if count == 0:
                can = n

            if n == can:
                count += 1

            else:
                count -= 1  
        return can          




        