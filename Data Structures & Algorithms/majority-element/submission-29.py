class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map1 = {}
        fre = 0
        for n in nums:
            map1[n] = map1.get(n, 0) + 1
            fre = max(map1[n], fre)
            if fre > len(nums)/2:
                return n
            

        