# Last updated: 8/5/2025, 2:55:53 PM
class Solution:
    def missingElement(self, nums, k):
        if len(nums) == 0:
            return 0
        missing, i, j = 0, 1, 1
        while k != 0 and i < len(nums):
            if nums[i] == nums[0] + j:
                j += 1
                i += 1
            else:
                k -= 1
                j += 1
        if k != 0:
            return nums[0] + j - 1 + k
        return nums[0] + j - 1