# Last updated: 8/5/2025, 2:56:39 PM
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # #Brute force (TC: O(nm), SC: O(1))
        # speed = 1

        # while True:
        #     hours_spent = 0
        #     for pile in piles:
        #         hours_spent += math.ceil(pile / speed)

        #     if hours_spent <= h:
        #         return speed 
        #     else:
        #         speed += 1 
                
        #Binary search (Time Complexity: O(n * log m), Space Complexity: O(1))
        left = 1
        right = max(piles)

        while left < right:
            hours_spent = 0
            mid = (left + right) // 2

            for pile in piles:
                hours_spent += math.ceil(pile / mid)

            if hours_spent <= h:
                right = mid 
            else:
                left = mid + 1 

        return right