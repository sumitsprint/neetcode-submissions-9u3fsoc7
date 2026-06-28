class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        b = 0

        left = 0
        right = len(people) - 1

        while left <= right:
            total = people[left] + people[right]

            if total <= limit:
                left += 1
                



                
            b += 1 
            right -= 1   
        return b    



        