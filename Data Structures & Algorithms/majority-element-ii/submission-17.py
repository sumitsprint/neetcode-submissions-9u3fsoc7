class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        occ = {}
        for n in nums:
            occ[n] = occ.get(n, 0) + 1
        res = []
        for key, value in occ.items():
            if value >  len(nums) // 3:
                res.append(key)
        return res           
            
        