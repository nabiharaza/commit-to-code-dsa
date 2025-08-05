// Last updated: 8/5/2025, 2:55:47 PM
class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        std::make_heap(stones.begin(), stones.end());

        while(stones.size() > 1) {
            auto heaviest_stone = stones.front();
            std::pop_heap(stones.begin(), stones.end());
            stones.pop_back();
    
            auto second_heaviest_stone = stones.front();
            std::pop_heap(stones.begin(), stones.end());
            stones.pop_back();

            if (heaviest_stone == second_heaviest_stone) {
                continue;
            }

            heaviest_stone -= second_heaviest_stone;
            stones.push_back(heaviest_stone);
            std::make_heap(stones.begin(), stones.end());
        }

        int last_stone;
        if (stones.size() == 1) {
            last_stone = stones[0];
        } else {
            last_stone = 0;
        }
        return last_stone;
    }
};