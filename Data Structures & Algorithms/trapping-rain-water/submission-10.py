class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = [0 for _ in range(n)]
        
        left = 1
        right = n - 2
        

        while left <= right:

            left_max = max(height[:left])
            right_max = max(height[right+1:])

            if left_max < right_max:
                water = left_max - height[left]
                res[left] = max(0, water)
                left += 1
            else:
                water = right_max - height[right]
                res[right] = max(0, water)
                right -= 1


                



            
            
            

                
                

        return sum(res) 

        
        