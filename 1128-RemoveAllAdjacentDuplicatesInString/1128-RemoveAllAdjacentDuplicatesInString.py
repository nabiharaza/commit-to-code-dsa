# Last updated: 8/5/2025, 2:55:42 PM
class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack, index = [], 0

        while index < len(S):
            if len(stack) > 0 and S[index] == stack[-1]:
                stack.pop()
            else:
                stack.append(S[index])
            index += 1
        return ''.join(stack)