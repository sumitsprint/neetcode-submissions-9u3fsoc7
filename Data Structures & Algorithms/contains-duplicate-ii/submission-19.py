class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        seen = set()
        
        for i in range(len(nums)):
            # 1. If the window exceeds size k, remove the oldest element
            if i > k:
                seen.remove(nums[i - k - 1])
            
            # 2. Check if the current element is a duplicate within the window
            if nums[i] in seen:
                return True
            
            # 3. Add the current element to the window
            seen.add(nums[i])
            
        return False
        