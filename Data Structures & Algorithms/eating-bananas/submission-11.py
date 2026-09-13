class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left <= right:

            mid = (left + right) // 2 #eating rate
            total_hrs = 0


            for pile in piles:
                hours = pile // mid
                if pile % mid:
                    hours += 1
                total_hrs += hours

            if total_hrs > h:
                left = mid + 1 #eating rate too slow or not valid
            else:
                right = mid - 1 #eating rate is valid
        return left 




            
        