# Last updated: 8/5/2025, 2:53:51 PM
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing_values = []
        index_pointer_to_next_value = 0
        curr = 1
        count = 0
        while index_pointer_to_next_value <= len(arr) - 1:
            if curr != arr[index_pointer_to_next_value]:
                count += 1
                missing_values.append(curr)
                if count == k:
                    return curr
                curr += 1
            else:
                index_pointer_to_next_value += 1
                curr += 1
        while count != k:
            count += 1
            if count == k:
                return curr
            curr += 1