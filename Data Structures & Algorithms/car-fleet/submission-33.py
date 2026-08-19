class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = list(zip(position, speed))

        cars.sort()
        time = []

        for pos, speed in cars:
            d = target - pos
            time.append(d/speed)
        
        if not time:
            return 0

        ans = []
        ans.append(time[-1])


        for i in range(n-2, -1, -1):
            if ans[-1] < time[i]:
                ans.append(time[i])
        return len(ans)        

        
        
        
        