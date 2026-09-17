class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)
        

        while left <= right:
            mid = (left + right) // 2

            current_sum = 0
            sub_array = 1
            i =0 
            while i < len(nums):
                if current_sum + nums[i] <= mid:
                    current_sum += nums[i]
                    i += 1
                else:
                    sub_array += 1
                    current_sum = 0
            if sub_array > k:
                left = mid + 1
            else:
                right = mid - 1    
        return left        
        
                    







        


        