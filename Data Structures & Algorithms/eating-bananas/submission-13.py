class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left <= right:
            mid = (left + right) // 2

            hr = 0
            thr = 0

            for pile in piles:
                thr += pile // mid
                if pile % mid:
                    thr += 1
            if thr > h:
                left = mid + 1
            else:
                right = mid - 1
        return left                    



        