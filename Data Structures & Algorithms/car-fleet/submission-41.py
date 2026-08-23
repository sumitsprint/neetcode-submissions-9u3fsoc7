class Solution:
    def carFleet(self, target: int, pos: List[int], speed: List[int]) -> int:
        n = len(pos)

        c = list(zip(pos,speed))
        c.sort()
        time = []
        ans = []

        for pos, speed in c:
            time.append((target - pos)/speed)
        if not time:
            return 0    

        ans.append(time.pop())    

        for i in range(len(time)-1,-1,-1):
            if ans[-1] < time[i]:
                ans.append(time[i])
        return len(ans)        



        

        
        