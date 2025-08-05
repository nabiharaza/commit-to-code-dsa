# Last updated: 8/5/2025, 2:52:28 PM
import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.min_num = 1

    def popSmallest(self) -> int:
        if self.heap:
            return heapq.heappop(self.heap)
        self.min_num += 1
        return self.min_num - 1

    def addBack(self, num: int) -> None:
        if self.min_num > num and num not in self.heap:
            heapq.heappush(self.heap, num)

# Tc - O(log n)
# Sc - O(N)
# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
    # def __init__(self):
    #     self.heap = []
    #     self.heap_set = set()
    #     self.max = 1
    
    # def popSmallest(self) -> int:
    #     if not self.heap:
    #         store = self.max
    #         self.max += 1 
    #         return store
    #     self.heap_set.remove(self.heap[0])
    #     return heapq.heappop(self.heap)
    
    # def addBack(self, num: int):
    #     if ((num > 0)
    #       and (num < self.max)
    #       and (num not in self.heap_set)):
    #         heapq.heappush(self.heap, num)
    #         self.heap_set.add(num)