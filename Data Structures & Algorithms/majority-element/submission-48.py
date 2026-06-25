class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = None
        count =  0

        for n in nums:
            if count == 0:
                c =  n
            if c == n:
                count += 1
            else:
                count -= 1

        count = 0
        for n in nums:
            if n == c:
                count += 1   
        if count > len(nums) // 2:
            return c             
        # return c     




        