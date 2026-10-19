class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        if n < k:
            return 0
        curr_sum = 0
        max_sum = 0
        see = set()
        left = 0
        for i in range(n):
            while nums[i] in see:
                see.remove(nums[left])
                curr_sum = curr_sum - nums[left]
                left += 1
                

            see.add(nums[i]) 
            curr_sum += nums[i] 
            if len(see) > k:
                see.remove(nums[left])
                curr_sum = curr_sum - nums[left]
                left += 1  
            if len(see) == k:
                max_sum = max(curr_sum, max_sum)

        return max_sum      



