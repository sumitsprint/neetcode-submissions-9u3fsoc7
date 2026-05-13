class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occ = {}
        m = 0
        for n in nums:
            occ[n] = occ.get(n , 0) + 1
            m = max(m, occ.get(n, 0))
            if m > len(nums) / 2:
                return n
        