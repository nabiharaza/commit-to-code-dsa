// Last updated: 8/5/2025, 2:57:02 PM
class Solution {
    public boolean rotateString(String A, String B) {
        StringBuffer tempA = new StringBuffer(A);
        
        if(A == null || B == null){
            return false; 
        } 
        else if(A.length() != B.length()){
            return false;
        }        
        else if(A.length() == 0){
            return true;
        } 
        else{
            for(int i=0; i<A.length(); i++){
                char judge = A.charAt(i);
                tempA.delete(0,1);
                tempA.append(judge);

                if(tempA.toString().compareTo(B) == 0) return true;
            }
        return false;
        }      
    }
}