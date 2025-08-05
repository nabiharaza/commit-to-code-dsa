// Last updated: 8/5/2025, 2:54:26 PM
class Solution {
    public int maxLength(List<String> arr) {
        return dfs(arr, "", 0);
    }
    
    int dfs(List<String> arr, String s, int index) {
        
        HashSet<Character> set = new HashSet<Character>();
        for(char c:  s.toCharArray())
            set.add(c);
        if(s.length() != set.size())
            return 0;
        
        int res = s.length();
        for(int i=index; i<arr.size(); i++) {
            res = Math.max(res, dfs(arr, s+arr.get(i), i+1));
        }
        return res;
        
    }
}