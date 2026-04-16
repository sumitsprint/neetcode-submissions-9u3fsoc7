class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # preMap = {}
        # for i, n in enumerate(nums):
        #     diff = target - n
        #     if diff in preMap:
        #         return [preMap[diff], i]
        #     preMap.update({n:i})
        # return  
        sum =0  
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums),1):
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i,j]


        # TC-    O(n) #
        # SC- O(n) 

            
        