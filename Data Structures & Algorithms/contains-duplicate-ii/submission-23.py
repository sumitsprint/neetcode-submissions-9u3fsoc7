class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        
        for i in range(len(nums)):
            # 1. Check
            if nums[i] in seen:
                return True
            
            # 2. Add
            seen.add(nums[i])
            
            # 3. Evict the oldest element if the window is now full
            # (e.g., if k=2, when i=2, the element at index 0 is now out of range)
            if len(seen) > k:
                seen.remove(nums[i - k])
                
        return False



        # tc O(n)
        # sc O(min(n,k))
        # The Small Array Exception: If the entire array size $n$ is smaller than $k$, the set will simply grow to size $n$ and never trigger the eviction step.Therefore, the maximum memory allocated for the hash set is bounded by whichever number is smaller: the window size $k$ or the total elements $n$.