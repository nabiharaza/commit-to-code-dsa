// Last updated: 8/5/2025, 2:56:07 PM
class Solution {
public:
    std::vector<std::vector<int>> kClosest(std::vector<std::vector<int>>& points, int k) {
        // Min Heap.
        std::priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> priority_queue;

        // Add to min heap.
        for (int i = 0; i < points.size(); i ++) {
            double distance = points[i][0]*points[i][0] + points[i][1]*points[i][1];
            priority_queue.emplace(distance, i);
            // priority_queue.push({distance, i});

            // One way is to maintain a queue of size k by continually checking if the size is k.
            // The logic is to make subsequent additions cheaper, since addition to a priority queue is O(logn)
            // HOWEVER, for large n (say all between 256 and 512), logn value remains mostly the same, but the addition
            // of an if is an O(n) computation expense, which significantly slows down the code.
        }

        // Result vector.
        std::vector<std::vector<int>> k_closest_points;

        // Pop from priority_queue.
        for (int i = 0; i < k; i++) {
            auto point = priority_queue.top();
            priority_queue.pop();
            
            k_closest_points.push_back(points[point.second]);
        }

        return k_closest_points;
    }
};