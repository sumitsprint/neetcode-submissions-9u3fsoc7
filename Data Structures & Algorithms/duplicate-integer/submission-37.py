class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] ==  nums[i - 1]:
                return True
            
        return False        
# T.C- O(n log n)
# S.C - O(1) or O(n)
# python's sort may use O(n) extra space internally.