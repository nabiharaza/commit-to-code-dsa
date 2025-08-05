// Last updated: 8/5/2025, 2:56:42 PM
#include <algorithm> // for std::max
#include <cmath> // for std::ceil
#include <iostream>
#include <vector>

/*
    Leetcode 875 Koko Eating Bananas
    Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas.
    The guards have gone and will come back in h hours.
    Koko can decide her bananas-per-hour eating speed of k.
    Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas,
    she eats all of them instead and will not eat any more bananas during this hour.
    Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
    Return the minimum integer k such that she can eat all the bananas within h hours.

    Steps:
    Get the min speed possible mathematically using ceiling function. ceil(total bananas / h)
    Answer will be greater than this.

    Get max speed = biggest pile
    This is the start and the end of the array for binary search.
    Lower end if the time to eat is <= h.
        Store this speed of this middle speed if it is lower than the previous minimum.
    Increase start if time to eat > h.
*/
class Solution {
public:
    int minEatingSpeed(std::vector<int>& piles, int h) {
        // Initialize total number of bananas.
        long int total_bananas = 0;

        // Get total number of bananas. O(n)
        for (auto pile : piles){
            total_bananas += pile;
        }

        // Minimum speed required to eat the bananas mathematically.
        int min_speed_possible = std::ceil(static_cast<double>(total_bananas) / h);
        // Get biggest pile.
        auto biggest_pile = std::max_element(piles.begin(), piles.end());

        // Get max possible speed.
        int max_speed_possible = *biggest_pile;

        // Binary search from min_speed_possible to max_speed_possible for the right speed.
        int start = min_speed_possible, end = max_speed_possible;

        int min_speed = max_speed_possible;
        while (start <= end){
            // If start exceed ends, exit the loop.
            if (start > end) {
                // We are guaranteed to find the desired speed.
                break;
            }

            int middle = (start + end)/2;
            // Compute time required for eating bananas with middle speed.
            long int time_to_eat = 0;
            for (auto pile : piles){
                // If the time to eat becomes greater than h, break.
                // No need to calculate the total sum.
                if (time_to_eat > h){break;}
                time_to_eat += std::ceil(static_cast<double>(pile) / middle);
            }

            if (time_to_eat > h){
                // Indicates speed is too slow
                start = middle + 1;
                continue;
            }

            if (time_to_eat <= h){
                // time to eat matches given time.
                // Multiple speeds may achieve the same time, choose the smallest.
                min_speed = (min_speed > middle) ? middle : min_speed;
                end = middle - 1;
            }
            // Cannot consider the case of time_to_eat < h separately because of the edge case
            // piles = {312884470} and h = 312884469. The min speed (the answer) also takes time smaller than
            // h. So time_to_eat == h is never achieved and we break out of the loop.
            // We need to lower 'end' if we find time < or = to h.

        }
        return min_speed;
    }
};