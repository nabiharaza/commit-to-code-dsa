# Last updated: 8/5/2025, 2:56:48 PM
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        p1, p2 = len(s) - 1, len(t) - 1

        while p1 >= 0 or p2 >= 0:
            if p1 >= 0 and s[p1] == "#" or p2 >= 0 and t[p2] == "#":
                if p1 >= 0 and s[p1] == "#":
                    back_count = 2
                    while back_count > 0 and p1 >= 0:
                        p1 -= 1
                        back_count -= 1
                        if p1 >= 0 and s[p1] == "#":
                            back_count += 2

                if p2 >= 0 and t[p2] == "#":
                    back_count = 2
                    while back_count > 0 and p2 >= 0:
                        p2 -= 1
                        back_count -= 1
                        if p2 >= 0 and t[p2] == "#":
                            back_count += 2
            else:
                if p1 >= 0 and p2 >= 0 and s[p1] != t[p2]:
                    return False
                if (p1 >= 0) != (p2 >= 0):  # One is exhausted before the other
                    return False

                p1 -= 1
                p2 -= 1

        return True