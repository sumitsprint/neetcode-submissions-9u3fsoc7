class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occ = {}
        for n in nums:
            if n in occ:
                occ[n]= occ.get(n, 0) + 1
            else:
                occ[n] = 1    
        for n,i in occ.items():
            if occ[n] > len(nums)/2:
                return n       


        
        