class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix = [1 for _ in range(len(nums))]
        prefix = []
        ans = [1] * len(nums)
        suffix = [1] * len(nums)
        f = 1
        fs = 1

        for i in range(len(nums)):
           
            prefix.append(f)
             
            f *= nums[i]    
                

        for i in range(len(nums) - 1, -1, -1):
            suffix[i] = fs
            fs *= nums[i]


           

              
            



        for i in range(len(ans)):
            ans[i] = prefix[i] * suffix [i]    
        return ans    


        