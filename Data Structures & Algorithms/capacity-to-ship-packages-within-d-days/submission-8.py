class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left <= right:
            mid = (left + right) // 2

            i =0
            wt = 0
            d = 1
            while i <len(weights):
                if wt + weights[i] <= mid:
                    wt += weights[i]
                    i += 1
                
                else:
                    d += 1
                    wt = 0

            if d > days:
                left = mid + 1
            else:
                right = mid - 1
        return left                    




        