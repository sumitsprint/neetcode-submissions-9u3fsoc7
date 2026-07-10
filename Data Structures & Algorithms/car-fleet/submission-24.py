class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        n = len(position)
        # Pair each car's starting position with its speed
        cars = list(zip(position, speed))

        # Sort cars by their starting position in ascending order
        cars.sort()
        time = []
        
        ans  = []

        # Calculate the time required for each car to reach the target individually
        for key, value in cars:
            d = target - key
            time.append(d / value)

        if not time:
            return 0    

        
        # Start tracking fleets from the car closest to the target (processed in reverse)
        ans.append(time[n-1])
        for i in range(n-2, -1, -1):
            
            
            # If a car behind takes more time, it cannot catch up and forms a new fleet
            if time[i] > ans[-1]:
                ans.append(time[i])

        return len(ans)