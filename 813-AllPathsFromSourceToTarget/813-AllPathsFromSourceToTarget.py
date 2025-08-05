# Last updated: 8/5/2025, 2:57:00 PM
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        N = len(graph)
        def solve(node):
            if node == (N - 1):
                return [[N - 1]]
            ans = []
            for neighbour in graph[node]:
                for path in solve(neighbour):
                    ans.append([node] + path)
            return ans
        return solve(0)