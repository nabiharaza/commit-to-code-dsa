# Last updated: 8/5/2025, 2:56:36 PM
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)

        left, right = 0, len(people)-1

        boats = 0

        # 3 2 2 1. - 3
        while left <= right:

            if people[left] + people[right] <= limit:
                right -= 1
            left += 1
            boats += 1
        
        return boats