class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        # nums[k] = nums[0]
        
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k+=1
        return k        



       



        # k = 0
        # for i in range(len(nums)):
        #     if nums[i] != val:
        #         nums[k] = nums[i]
        #         k = 1 + k
        # return k         

        