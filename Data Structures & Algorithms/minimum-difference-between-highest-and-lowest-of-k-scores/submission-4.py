class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        nums.sort()    
        min_ = float('inf')
        n = len(nums)

        for i in range(n-k+1):
            min_ = min(nums[i+k-1] - nums[i], min_)
        return min_    


        