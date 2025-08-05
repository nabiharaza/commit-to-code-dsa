# Last updated: 8/5/2025, 2:54:55 PM
class Solution:
    def tribonacci(self, n: int) -> int:
        dp = {0:0, 1:1, 2:1}
        def dfs(n):
            if n in dp:
                return dp[n]
            dp[n] = dfs(n-1) + dfs(n-2) + dfs(n-3)
            return dp[n]

        return dfs(n)



# Example
# n = 4
# T4 = T3 + T2 + T1
#     = 2 + 1 + 1 = 4


# T3 = T2 + T1 + T0
#     = 1 + 1 + 0
#     = 2