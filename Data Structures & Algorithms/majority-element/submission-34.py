class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxC =0
        occ = {}
        for n in nums:
            occ[n]=occ.get(n, 0) + 1
            maxC = max(occ.get(n,0), maxC)
            if maxC> len(nums)/2:
                return n
        