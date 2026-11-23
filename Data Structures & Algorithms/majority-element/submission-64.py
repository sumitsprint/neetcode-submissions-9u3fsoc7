class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count1 = 0
        cand = None
        for n in nums:
            if count1 == 0:
                cand = n 
            if n == cand:
                count1 += 1
            else:
                count1 -= 1
        return cand            


        