class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        x = len(nums)
        seen = set()
        for i in range(x):
            
            if nums[i] in seen:
                return True

            seen.add(nums[i])    
            if i >= k:
                seen.remove(nums[i-k])
        return False               







        


        