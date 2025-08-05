# Last updated: 8/5/2025, 2:53:55 PM
# Sliding window

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        num_zeros = 0
        max_window = 0

        for right in range(len(nums)):
            # print('left', left)
            # print('right', right)

            if nums[right] == 0:
                num_zeros += 1

            while num_zeros > 1:
                if nums[left] == 0:
                    num_zeros -= 1
                left += 1
                # print('new left', left)

            window = right - left
            # print('window', window)
            max_window = max(window, max_window)
            # print('max_window', max_window)

        return max_window

# tc - o(n)
# sc - o(1)