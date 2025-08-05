# Last updated: 8/5/2025, 2:54:36 PM
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        a = list(s)
        stack = []
        flag = False
        while len(s) > 0 and not flag:
            for ele in range(len(a)):
                if ele == 0 or a[ele] != a[ele - 1]:
                    stack.append(1)
                else:
                    val = stack.pop() + 1
                    if val == k:
                        start = (ele - k + 1)
                        for i in range(start, ele + 1):
                            a[i] = '%'
                    else:
                        stack.append(val)
            temp = ''.join(a)
            temp = temp.replace('%','')
            if temp == s:
                flag = True
            s = temp
            a = list(s)
        return s