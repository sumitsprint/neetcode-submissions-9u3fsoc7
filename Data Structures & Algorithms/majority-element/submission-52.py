class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cc = None
        count  = 0

        for n in nums:
            if count == 0:
                cc = n
            if n == cc:
                count += 1

            else:
                count -= 1
        return cc        





        