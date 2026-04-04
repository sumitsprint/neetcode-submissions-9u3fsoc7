class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      
        hashset = set()
        for n in nums:
            if n in hashset:
                return True

            hashset.add(n)
        return False
        """  nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False"""