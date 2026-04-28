class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cc, co =0, 0
        for n in nums:
            if co == 0:
                cc = n
            if n == cc:
                co += 1
            else:
                co -= 1
        return cc                
        