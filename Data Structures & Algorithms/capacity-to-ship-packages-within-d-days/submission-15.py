class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left <= right:
            mid  = (left + right) // 2

            current_weight = 0
            d = 1
            i = 0

            #checking weight capacity
            while i < len(weights):
                if weights[i] + current_weight <= mid:
                    current_weight += weights[i]
                    i += 1
                else:
                    d += 1
                    current_weight = 0

            #validity of weight capacity
            if d > days:
                left = mid + 1

            else:
                right = mid - 1
        return left                






                



        