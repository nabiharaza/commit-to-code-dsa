# Last updated: 8/5/2025, 2:56:06 PM
import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def euclidean_with_origin(point):
            return math.sqrt((point[0])**2 + (point[1])**2)
        
        points.sort(key=euclidean_with_origin)
        
        return points[:k]

