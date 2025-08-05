# Last updated: 8/5/2025, 2:52:24 PM
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        pq1 = []
        pq2 = []
        i = 0
        j = len(costs) - 1
        ans = 0

        while k > 0:
            # print("k", k)
            while len(pq1) < candidates and i <= j:
                heapq.heappush(pq1, costs[i])
                i += 1
                # print(pq1)

            while len(pq2) < candidates and i <= j:
                heapq.heappush(pq2, costs[j])
                j -= 1
                # print(pq2)

            t1 = pq1[0] if pq1 else float('inf')
            # print(t1)
            t2 = pq2[0] if pq2 else float('inf')
            # print(t2)

            if t1 <= t2:
                ans += t1
                # print(ans)
                heapq.heappop(pq1)
                # print(pq1)
            else:
                ans += t2
                # print(ans)
                heapq.heappop(pq2)
                # print(pq2)

            k -= 1

        return ans