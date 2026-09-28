class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        see = set()

        for i in range(len(nums)):
            if nums[i] in see:
                return True
            see.add(nums[i])
            if len(see) == k + 1:
                see.remove(nums[i-k])
        return False        



            
            
            



        
        