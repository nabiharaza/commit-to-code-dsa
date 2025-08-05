# Last updated: 8/5/2025, 2:54:35 PM
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        charCount = 0
        for i in range(len(s)):
            if s[i] == 'R':
                charCount += 1
            else:
                charCount -= 1
            if charCount == 0:
                balance += 1
        return balance