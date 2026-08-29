class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        # ans = []
        
        


        while left <= right:
            thr = 0
            

            mid = (left + right) // 2 # candidate eating rate

            for n in piles:
                hr = n // mid
                hro = n % mid
                if hro > 0:

                    hr += 1
                
                thr += hr 
            if thr <= h:
                right = mid - 1
            else:
                #If mid is too slow, which side of the search space contains the speeds that might work?
                left = mid + 1

                   

                #right moves left whenever mid is valid.
# left moves right whenever mid is too slow.

            


                     
                
               


        return left  




            








            


        
        