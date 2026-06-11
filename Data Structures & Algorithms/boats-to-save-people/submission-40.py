class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()

        left = 0
        right = n - 1
        boats = 0

        while left <= right:
            total = people[left] + people[right]

            if total <= limit:
                left += 1

            
            right -= 1
            boats += 1
        return boats        








        