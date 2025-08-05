// Last updated: 8/5/2025, 2:56:01 PM
class TimeMap {
public:
    /**
     * @brief Constructor.
     */
    TimeMap() {

    }

    /**
     * @brief
     */
    void set(std::string key, std::string value, int timestamp) {
        // Add the timestamp-value pair to the vector mapped by the key.
        time_based_key_value_map[key].emplace_back(std::pair<int, std::string>(
            timestamp, value));
    }

    std::string get(std::string key, int timestamp) {
        // Get size of the vector at key to search.
        int num_stamps = time_based_key_value_map[key].size();

        // Initialize pointers for binary search.
        int left = 0, right = num_stamps - 1;

        // O(logn) search
        while(left <= right) {
            // If left exceed right, break out of the loop.
            if (left > right) {
                break;
            }

            // Calculate middle position.
            int middle = (left + right)/2;

            // If middle is timestamp, return it.
            if (timestamp == time_based_key_value_map[key][middle].first) {
                return time_based_key_value_map[key][middle].second;
            }

            // If timestamp greater than middle, go right.
            if (timestamp > time_based_key_value_map[key][middle].first) {
                left = middle + 1;
                continue;
            }

            // If timestamp smaller than middle, go left.
            if (timestamp < time_based_key_value_map[key][middle].first) {
                right = middle - 1;
                continue;
            }
        }  // while loop ends, binary search over.

        // Return the value pointed by the right pointer.
        if (right < 0) {
            // If the requested timestamp is smaller than the smallest available.
            return "";
        }
        return time_based_key_value_map[key][right].second;
    }

private:
    // Time Based Key Value Hashmap.
    std::unordered_map<std::string, std::vector<std::pair<int, std::string>>> time_based_key_value_map;
};