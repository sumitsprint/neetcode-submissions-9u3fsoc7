class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        f = 1
        s = []
        ans = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            if nums[i] == 0:
                s.append(i)
                continue
            f *= nums[i]

        for i in range(len(ans)):
            if len(s) > 1:
                return ans
            if len(s) == 1:    
                if i == s[0]:
            
                    ans[i] = (ans[i]) + f
                # else:
                #     ans[i] = 0
            else:
                ans[i] = ans[i] + (f // nums[i])            
        return ans
        
            # ans[i] = (ans[i]) + f / nums[i] if nums[i] > 0 else 0    
        
            
            
        
        
        

        # return ans         