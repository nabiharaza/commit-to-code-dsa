// Last updated: 8/5/2025, 2:55:44 PM
class Solution {
    public String removeDuplicates(String S) {
        Stack <Character> stack = new Stack<Character>();
        for(int i=0; i<S.length(); i++){
            if(!stack.isEmpty() && S.charAt(i) == stack.peek()){
                stack.pop();
            } else {
                stack.push(S.charAt(i));
            }
        }
        StringBuffer result = new StringBuffer();
        for(char c:stack){
            result.append(c);
        }
        return result.toString();
    }
}