# Last updated: 8/5/2025, 2:52:51 PM
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []
        max_height = 0
        for i in range(len(heights)-1,-1,-1):
            if heights[i] > max_height:
                res.append(i)
                max_height = heights[i]
        
        return sorted(res)