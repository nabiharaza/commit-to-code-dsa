# Last updated: 8/5/2025, 2:52:16 PM
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        left_ptr = -1
        dup_ptr = -1
        distinct_elements = set()
        count = 0
        idx = 0
        while left_ptr < len(nums) and dup_ptr < len(nums) and idx < len(nums):
            if nums[idx] not in distinct_elements:
                distinct_elements.add(nums[idx])
                idx += 1
            else:
                dup_ptr = idx
                while nums[idx] in distinct_elements and left_ptr + 1 < dup_ptr:
                    if left_ptr+3 < len(nums) and nums[left_ptr+3] in distinct_elements:
                        distinct_elements.remove(nums[left_ptr+3])
                    if left_ptr+2 < len(nums) and nums[left_ptr+2] in distinct_elements:
                        distinct_elements.remove(nums[left_ptr+2])
                    if left_ptr+1 < len(nums) and  nums[left_ptr+1] in distinct_elements:
                        distinct_elements.remove(nums[left_ptr+1])
                    left_ptr += 3
                    count += 1
                dup_ptr = left_ptr + 1
                idx = dup_ptr
                distinct_elements.clear()
        return count