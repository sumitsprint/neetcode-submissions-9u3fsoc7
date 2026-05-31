class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        l = 0
        r = n - 1
        boats = 0

        while l <= r:
            weight = people[l] + people[r]
            if weight <= limit:
                l += 1
                
            
            r -= 1
            boats += 1
        return boats        

        