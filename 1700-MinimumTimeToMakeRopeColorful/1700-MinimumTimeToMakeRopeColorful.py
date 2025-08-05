# Last updated: 8/5/2025, 2:53:41 PM
class Solution:
    def minCost(self, S: str, B: List[int]) -> int:
        min_cost = 0
        for i in range(0, len(S) - 1):
            if S[i + 1] == S[i]:
                if B[i] > B[i + 1]:
                    min_cost += B[i + 1]
                else:
                    min_cost += B[i]
                if B[i] > B[i + 1]:
                    B[i + 1] = B[i]
        return min_cost