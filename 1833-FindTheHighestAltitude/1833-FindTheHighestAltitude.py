# Last updated: 8/5/2025, 2:53:00 PM
# prefix sum

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_altitude = highest_altitude = 0

        for altitude_gain in gain:
            current_altitude += altitude_gain
            highest_altitude = max(highest_altitude, current_altitude)
            # print(highest_altitude)

        return highest_altitude

# tc -  o(n)
# sc - o(1)

