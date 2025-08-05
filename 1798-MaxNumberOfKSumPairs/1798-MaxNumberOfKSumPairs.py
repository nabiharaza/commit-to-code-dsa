# Last updated: 8/5/2025, 2:53:04 PM
class Solution():
    def maxOperations(self, nums, k):
        nums.sort()
        count = 0
        left = 0
        right = len(nums) - 1

        while left < right:
            sum = nums[left] + nums[right]
            if sum == k:
                count += 1
                left += 1
                right -= 1
            elif sum < k:
                left += 1
            else:
                right -= 1
            
        return count

# tc - o(n log n) + o (n) = o (n log n)
# sc - o(n) or o(log n)