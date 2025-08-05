// Last updated: 8/5/2025, 2:54:41 PM
class Solution {
    public String reverseParentheses(String s) {
        Stack <Character> stack = new Stack<>();
        for(char c: s.toCharArray()){
            if(c==')'){
                Queue <Character> p = new LinkedList<>();
                while(!stack.isEmpty() && stack.peek() !='(') 
                    p.add(stack.pop());
                if(!stack.isEmpty())
                    stack.pop();
                while(!p.isEmpty())
                    stack.push(p.remove());
            } else {
                stack.push(c);
            }
        }
        StringBuilder sb = new StringBuilder();
        while(!stack.isEmpty())
            sb.append(stack.pop());
        return sb.reverse().toString();
    }
}