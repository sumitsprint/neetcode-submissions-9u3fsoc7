class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()

        n = len(people)
        left = 0
        right = n - 1

        paired_boats = 0

        while left <= right:
            total_weight = people[left] + people[right]

            if total_weight <= limit:
                
                left += 1
                right -= 1

            else:

                right -= 1
                
            paired_boats += 1    

        # paired_people = paired_boats * 2
        # unpaired_people = n - paired_people

        # total_boats = paired_boats + unpaired_people

        return paired_boats

        """ greedy algo Sort.
Try to pair lightest with heaviest.
Count successful pairs.
Everyone else gets their own boat.
"""
# Time: O(n log n)
# Space: O(1)