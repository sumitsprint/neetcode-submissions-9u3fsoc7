class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)

        cars = list(zip(position,speed))

        cars.sort()
        ans = []
        time = []

        for k, v in cars:
            d = target - k
            time.append(d/v)

        if not time:
            return 0


        ans.append(time[-1])

        for i in range(n-2,-1,-1):
            if time[i] > ans[-1]:
                ans.append(time[i])

        return len(ans)        




        
                
        
            
        
            







        
        