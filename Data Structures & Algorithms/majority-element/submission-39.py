class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        cc = None
        
        for n in nums:
            if count == 0: #empty slot
                cc = n
            if n == cc:
                count += 1
            else:
                count -= 1
        return cc            

        