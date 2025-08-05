# Last updated: 8/5/2025, 2:53:50 PM
class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        if high%2 == 0 and low%2 == 0:
            return (high-low)/2
        else:
            return int(high-low)/2 + 1