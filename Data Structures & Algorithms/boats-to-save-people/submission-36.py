class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1
        b=0

        while l <= r:
            t = people[l] + people[r]
            if t <= limit:
                l+=1
            r -= 1
            b +=1
        return  b       




        