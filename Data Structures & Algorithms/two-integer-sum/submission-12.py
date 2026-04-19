class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        flyMap={}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in flyMap:
                return [flyMap[diff], i]
            flyMap.update({n:i})    


        
        
        

        