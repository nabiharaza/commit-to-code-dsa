# Last updated: 8/5/2025, 2:56:45 PM
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        low, high = 0, len(A) - 1
        while low < high:
            mid = (low + high) // 2
            if A[mid] < A[mid + 1]:
                low = mid + 1
            else:
                high = mid
        return low