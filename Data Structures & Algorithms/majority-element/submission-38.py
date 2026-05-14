class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occ = {}
        maxCount = 0
        for n in nums:
            occ[n] = occ.get(n, 0) + 1  
            maxCount = max(occ.get(n, 0), maxCount)
            if maxCount > len(nums)//2:
                return n 
               


        
        