# Last updated: 8/5/2025, 2:52:36 PM
from collections import Counter
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        # "bbcbaba"
        # b 4, c 1, a 2
        # > 3 count 1
        # (for all >=2 )itself twice + all of the rest atleast one
        
        result = 0

        for middle in set(s):
            first = s.find(middle)
            last = s.rfind(middle)

            if last - first >= 2:
                for unique in set(s[first+1:last]):
                    result += 1
        return result




