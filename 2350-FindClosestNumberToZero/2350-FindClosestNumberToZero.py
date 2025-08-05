# Last updated: 8/5/2025, 2:52:30 PM
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        
        min_distance = float('inf')
        min_dist_nums = set()
        for num in nums:
            if abs(num) < min_distance:
                min_distance = abs(num)
                min_dist_nums.clear()
                min_dist_nums.add(num)
            elif abs(num) <= min_distance:
                min_dist_nums.add(num)

            
        return max(min_dist_nums)
