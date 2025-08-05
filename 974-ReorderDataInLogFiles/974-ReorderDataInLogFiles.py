# Last updated: 8/5/2025, 2:56:22 PM
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digitLogs, letterLogs = [], []
        for log in range(len(logs)):
            if logs[log].split()[1].isdigit():
                digitLogs.append(logs[log])
            else:
                letterLogs.append(logs[log].split())
        print(letterLogs)
        letterLogs.sort(key=lambda x: x[0])
        letterLogs.sort(key=lambda x: x[1:])
        for i in range(len(letterLogs)):
            letterLogs[i] = (" ".join(letterLogs[i]))
        return letterLogs + digitLogs