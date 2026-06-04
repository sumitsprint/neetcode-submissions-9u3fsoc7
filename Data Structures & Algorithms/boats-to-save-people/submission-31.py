class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)

        left = 0
        right = n - 1
        b = 0

        while left <= right:
            total = people[left] + people[right]
            if total <= limit:
                
                left += 1
                
        
            
            right -= 1    
            b+=1         
        return b    

        
        