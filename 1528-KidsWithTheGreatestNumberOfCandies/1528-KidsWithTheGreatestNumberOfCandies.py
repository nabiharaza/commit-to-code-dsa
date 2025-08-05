# Last updated: 8/5/2025, 2:54:03 PM
class Solution:
    def kidsWithCandies(self, candies: [], extraCandies: int) -> []:

        most_candies = max(candies)

        res = []
        for candy in candies:
            if candy + extraCandies >= most_candies:
                res.append(True)
            else:
                res.append(False)

        return res

# tc - o(n)
# sc - o(1)