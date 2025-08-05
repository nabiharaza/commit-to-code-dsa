# Last updated: 8/5/2025, 2:54:27 PM
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        remove = set()
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack:
                    stack.pop()
                else:
                    remove.add(i)

        remove = remove.union(set(stack))

        res = ""
        for i, char in enumerate(s):
            if i not in remove:
                res += char
        
        return res