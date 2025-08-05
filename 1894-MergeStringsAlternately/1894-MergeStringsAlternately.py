# Last updated: 8/5/2025, 2:52:54 PM
# using 2 pointers

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        mergedString = []
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                mergedString += word1[i]
                i += 1
            if j < len(word2):
                mergedString += word2[j]
                j += 1
        return ''.join(mergedString)

# tc - o(m+n), sc - o(1) or o(m+n)