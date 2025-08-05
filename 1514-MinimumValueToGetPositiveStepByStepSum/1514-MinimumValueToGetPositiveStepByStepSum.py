# Last updated: 8/5/2025, 2:54:06 PM
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        sum = 0
        ans = 0
        for i in range(len(nums)):
            sum += nums[i]
            ans = min(ans, sum)
        return abs(ans) + 1