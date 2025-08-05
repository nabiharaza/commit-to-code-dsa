# Last updated: 8/5/2025, 2:56:05 PM
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        for i in nums:
            x = i*i
            result.append(x)
        
        result = sorted(result)
        
        return result
        