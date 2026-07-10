from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        
        # Pair each car's starting position with its speed
        cars = list(zip(position, speed))

        # Sort the cars by their starting position in ascending order.
        # This allows us to process them from the car closest to the target backward.
        cars.sort()
        
        # Array to store the time it takes for each car to reach the target independently
        time = []
        
        # 'ans' acts as a stack to keep track of the bottleneck arrival times for each fleet
        ans = []

        # Calculate the time needed for each car to reach the target
        for key, value in cars:
            d = target - key        # Distance remaining to the target
            time.append(d / value) # Time = Distance / Speed

        # Edge case: If there are no cars, return 0
        if not time:
            return 0
        
        # Start by adding the time of the car closest to the target (the rightmost car)
        ans.append(time[n-1])
        
        # Iterate backwards from the second-to-last car down to the first car
        for i in range(n-2, -1, -1):
            
            # If the current car takes MORE time than the fleet ahead of it,
            # it will never catch up. Therefore, it forms a new fleet.
            if time[i] > ans[-1]:
                ans.append(time[i])
            
            # Note: If time[i] <= ans[-1], this car catches up to the fleet ahead.
            # It gets blocked by the slower car ahead and merges into that existing fleet.

        # The number of elements in the stack represents the total number of fleets
        return len(ans)