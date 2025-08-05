# Last updated: 8/5/2025, 2:54:29 PM

class Solution:
    def find(self, i, jobs, startTime, dp):
        if i >= len(jobs):
            return 0
        if dp[i] != -1:
            return dp[i]

        index = bisect_left(startTime, jobs[i][1])

        pick = jobs[i][2] + self.find(index, jobs, startTime,dp)
        notpick = self.find(i + 1, jobs, startTime, dp)
        dp[i] = max(pick, notpick)
        return dp[i]

    def jobScheduling(self, startTime, endTime, profit):
        # n = len(startTime)
        jobs =list(zip(startTime, endTime, profit))
        dp = [-1] * len(jobs)

        jobs.sort(key=lambda x: x[0])

        return self.find(0, jobs, [jobs[i][0]for i in range(len(jobs))], dp)
