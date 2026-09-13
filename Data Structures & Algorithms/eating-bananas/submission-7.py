class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        min_speed = 1
        max_speed = max(piles)
        
        while min_speed <= max_speed:
            total_hours = 0
            candidate_speed = (min_speed + max_speed) // 2
            
            for pile in piles:
                hours_for_pile = pile // candidate_speed
                remainder = pile % candidate_speed
                if remainder > 0:
                    hours_for_pile += 1
                
                total_hours += hours_for_pile
                
            if total_hours <= h:
                max_speed = candidate_speed - 1
            else:
                min_speed = candidate_speed + 1

        return min_speed