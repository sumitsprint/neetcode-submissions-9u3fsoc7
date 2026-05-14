class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        occ = {}
        maxCount = len(nums) // 3
        arr = []
        for n in nums:
            occ[n] = occ.get(n, 0) + 1


        for key, value in occ.items():
            if value > maxCount:
                arr.append(key)

            

        
        return arr      
             

                