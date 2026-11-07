class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left <= right:
            mid = (left + right) // 2

            shipped = 0
            d = 1 
            i = 0
            while i < len(weights):

                if shipped + weights[i] <= mid:

                    shipped += weights[i]
                    i += 1

                else:
                    d += 1
                    shipped = 0

            if d > days:
                left = mid + 1

            else:
                right = mid - 1
        return left                    




                








        