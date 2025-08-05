# Last updated: 8/5/2025, 2:55:43 PM
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        data = []
        for stone in stones:
            heapq.heappush(data, -stone)

        while len(data) > 1:
            x = -heapq.heappop(data)
            y = -heapq.heappop(data)

            if x == y:
                continue
            elif x < y:
                heapq.heappush(data, -(y-x))
            else:
                heapq.heappush(data, -(x-y))
        
        return -data[0] if data else 0
        