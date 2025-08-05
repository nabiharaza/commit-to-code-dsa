// Last updated: 8/5/2025, 2:54:52 PM
#include <string>
#include <vector>
class Solution {
public:
    int longestCommonSubsequence(std::string text1, std::string text2) {
        // Length of smaller string.
        int n1;

        // Length of bigger string.
        int n2;

        std::string small, big;

        if (text1.size() < text2.size()) {
            std::tie(n1, small) = std::make_pair(text1.size(), text1);
            std::tie(n2, big) = std::make_pair(text2.size(), text2);
        } else {
            std::tie(n1, small) = std::make_pair(text2.size(), text2);
            std::tie(n2, big) = std::make_pair(text1.size(), text1);
        }

        // DP Matrix of size n1 x n2.
        std::vector<std::vector<int>> dp_matrix(n1 + 1, std::vector<int>(n2 + 1, 0));

        // Dynamic Programming
        for (int i = 1; i <= n1; i++) {
            for (int j = 1; j <= n2; j++) {
                // // If string elements at ith and jth position are same.
                // int is_equal_increment = (small[i-1] == big[j-1]);
            
                // // Current position is max of previous neighbors + the increment.
                // dp_matrix[i][j] = std::max(dp_matrix[i-1][j], dp_matrix[i][j-1]) + is_equal_increment;

                if (small[i-1] == big[j-1]) {
                dp_matrix[i][j] = dp_matrix[i-1][j-1] + 1;
                } else {
                dp_matrix[i][j] = std::max(dp_matrix[i-1][j], dp_matrix[i][j-1]);
                }
            }
        } 

        return dp_matrix[n1][n2];     
    }
};