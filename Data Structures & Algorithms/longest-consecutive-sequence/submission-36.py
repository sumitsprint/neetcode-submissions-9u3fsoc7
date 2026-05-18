class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 1
        if len(nums) == 0:
            return 0    
        seen = set(nums)
        # seen.update(nums)
         
        
        m = 0

        

        for i in range(len(nums)):
            pe = nums[i] - 1
            if pe in seen:
                continue
            else:
                cs = 1
                m = max(m, cs)
                fe = nums[i] + 1
                while fe in seen:
                    cs += 1
                    m = max(m , cs)
                    fe += 1
                # cs = 0
        return m            
                


    # tc - O(n)

            
           
        