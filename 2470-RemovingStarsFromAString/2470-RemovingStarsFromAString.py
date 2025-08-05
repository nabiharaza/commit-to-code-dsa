# Last updated: 8/5/2025, 2:52:24 PM
class Solution:
    def removeStars(self, s: str) -> str:
        # stack = []
        # for i in range(0, len(s)):
        #     if s[i] == '*':
        #         stack.pop()
        #     else:
        #         stack.append(s[i])
        # return ''.join(stack)

        stack = []
        for ch in s:
            if ch == '*':
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)