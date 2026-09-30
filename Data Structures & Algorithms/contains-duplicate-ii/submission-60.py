class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        see = set()
        left = 0

        for i in range(len(nums)):
            if nums[i] in see:
                return True

            see.add(nums[i])

            if i - left + 1 > k:
                see.remove(nums[left])
                left += 1
        return False         

        