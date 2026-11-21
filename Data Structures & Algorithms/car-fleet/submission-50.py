class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        fleet = []
        cars = list(zip(position, speed))
        cars.sort()
        times = []

        for pos, speed in cars:
            dis = target - pos
            time = dis / speed
            times.append(time)

        if not time:
            return 0

        fleet.append(times[-1])

        for i in range(n-2, -1, -1):
            if times[i] > fleet[-1]:
                fleet.append(times[i])
        return len(fleet)                
           
        
            
        
                
            
            




        



        