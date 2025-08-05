// Last updated: 8/5/2025, 2:56:50 PM
class Solution {
    
    public boolean backspaceCompare(String S, String T) {
        return getString(S).equals(getString(T));
    }
    
    private String getString(String str) {
        int n = str.length(), count = 0;
        StringBuilder sb = new StringBuilder();
        for(int i=n-1; i>=0; i--) {
            char c = str.charAt(i);
            if(c == '#')
                count++;
            else {
                if(count > 0)
                    count--;
                else
                    sb.append(c);
            }
        }
        return sb.toString();
    }
    
}