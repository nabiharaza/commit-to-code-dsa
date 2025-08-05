# Last updated: 8/5/2025, 2:53:56 PM
#sliding window

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        count = max_count = 0

        for i in range(k):
            count += int(s[i] in vowels)
        max_count = count

        for i in range(k, len(s)):
            count += int(s[i] in vowels) - int(s[i - k] in vowels)
            max_count = max(max_count, count)

        return max_count

# tc - o(n), sc - o(1)