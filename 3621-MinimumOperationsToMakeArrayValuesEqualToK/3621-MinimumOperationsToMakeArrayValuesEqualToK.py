# Last updated: 8/5/2025, 2:52:15 PM
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        num_map = set()
        for i in range(len(nums)):
            if nums[i] < k:
                return -1
            elif nums[i] > k:
                num_map.add(nums[i])
            
        return len(num_map)