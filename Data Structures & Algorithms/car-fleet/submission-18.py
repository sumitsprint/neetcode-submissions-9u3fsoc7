class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        n = len(position)
        cars = list(zip(position, speed))

        cars.sort()
        time = []
        
        du = 0
        ans  = []

        for key, value in cars:
            d = target - key
            time.append(d / value)

        
        ans.append(time[n-1])
        for i in range(n-2, -1, -1):
            
            
            if time[i] > ans[-1]:
                ans.append(time[i])

        return len(ans)
                

            

                
            
            
                   

       

             


        

              
            

                

        
        