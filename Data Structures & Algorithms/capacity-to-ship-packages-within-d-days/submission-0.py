class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left <= right:
            mid = (left + right) // 2
            c_wt = 0
            d = 1
            i = 0

            
            while i < len(weights):

                if c_wt + weights[i] <= mid:
                    c_wt += weights[i]
                    i += 1

                else:




                    d += 1
                    c_wt = 0
            if d <= days:
                right = mid - 1

            else:
                left = mid + 1
        return left        



                    
            








                












        