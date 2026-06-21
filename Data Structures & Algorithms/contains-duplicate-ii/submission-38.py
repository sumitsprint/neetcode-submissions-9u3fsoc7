class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        see = set()

        left = 0
        for right in range(len(nums)):
            if nums[right] in see:
                return True
            see.add(nums[right])

            if len(see) > k:
                see.remove(nums[right-k])
        return False        


        