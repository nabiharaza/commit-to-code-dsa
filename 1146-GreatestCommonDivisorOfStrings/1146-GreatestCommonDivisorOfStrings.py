# Last updated: 8/5/2025, 2:55:39 PM
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        def valid(k):
            n1, n2 = len1 // k, len2 // k
            base = str1[:k]
            if str1 == n1 * base and str2 == n2 * base:
                return True

        for i in range(min(len1, len2), 0, -1):
            if valid(i):
                return str1[:i]

        return ""

    # tc - o(min(m, n) * (m + n))
    # sc - o(min(m, n))
