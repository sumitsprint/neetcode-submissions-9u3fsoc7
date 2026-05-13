class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 1
        if len(nums) == 0:
            return 0    
        seen = set()
        nums.sort()   
        cs =1
        m = 1

        i = 0
        j = i + 1

        while i< len(nums) - 1:
            # j = i + 1
            if nums[i+1] - nums[i] != 1 and nums[i+1] - nums[i] != 0:
                i += 1
                
                seen.clear()
            else:
                
                seen.add(nums[i])
                seen.add(nums[i+1])
                cs = len(seen)
                m = max(m, cs)
                i += 1
        return m        
                






        
            




        




        