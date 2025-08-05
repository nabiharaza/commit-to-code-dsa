// Last updated: 8/5/2025, 2:54:31 PM
class Solution {
    public int balancedStringSplit(String s) {
        int res = 0, count = 0;
        for(char c: s.toCharArray()) {
            count+= c == 'R' ? 1 : -1;
            if(count == 0)
                res++;
        }
        return res;
    }
}