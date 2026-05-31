class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        left = 0
        right = n - 1
        ans = 0
        
        while left < right:
            total = people[left] + people[right]
            if total <= limit:
                ans += 1
                left += 1
                right -= 1
            elif total > limit:
                right -= 1
            else:
                left += 1

        new_r = ans*2
        new_l = n - new_r
        ans = ans + new_l
        

        return ans                
            



        