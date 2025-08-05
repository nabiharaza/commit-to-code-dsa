// Last updated: 8/5/2025, 2:56:44 PM
#include <algorithm>
#include <iostream>
#include <vector>

/*
    The basic idea is to arrange all the cars in sorted order of position.
    Create a vector of pairs (position, speed) and sort it by position.
    Begin your loop from the car closest to the target.
    initialize fleet_set = {}
    while i >= 0; i --;
        1. curr pos = ith.
        2. time = time for p to reach target.
        3. Add curr pos to fleet_set.
        4. if next position car is not overtaking ->
            add fleet_set to result vector.
            fleet_set = {}

    return result.size()
*/

class Solution {
public:
    /**
     * @brief returns the number of car fleets that reach the target.
     * @param
     */
    int carFleet(int target, std::vector<int>& position, std::vector<int>& speed) {
        std::vector<std::pair<int, int>> cars;
        for (int p = 0; p < position.size(); p++){
            auto pos = position[p];
            auto sp = speed[p];
            cars.push_back({pos, sp});
        }

        // Sort cars (pos, speed pairs) by ascending order of position.
        std::sort(cars.begin(), cars.end());

        int num_car_fleets = 0;

        double time_max = 0.0;

        for (int i = cars.size() - 1; i >= 0; i--){
            double time = (double) (target - cars[i].first)/cars[i].second;

            std::cout<<"time "<<time<<" and max time = "<<time_max<<std::endl;
            if (time > time_max) {
                num_car_fleets++;
                time_max = time;
            }

            // // Check if we haven't reached the end.
            // if (i > 0) {
            //     double time_next = double (target - cars[i - 1].first)/cars[i - 1].second;
            //     if (time_next > time) {
            //         // the next car will not overtake the current car.
            //         // Any downstream car which is faster will be slowed down by this one.
            //         // So this car fleet ends here.

            //         // Increment the num_car_fleets here.
            //         num_car_fleets++;
            //     }
            // }
        }
        return num_car_fleets;
    }
};