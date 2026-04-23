class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occ = {}
        for n in nums:
            occ[n] = occ.get(n, 0) + 1
        for i, n in occ.items():
            if occ[i] > len(nums)/2:
                return i
        return        

        
        