// Last updated: 8/5/2025, 2:53:06 PM
public class Solution {


    public boolean canFormArray (int[] target , int[][] pieces) {

        int i = 0;
        int j = 0;
        int repeater = pieces.length;

        HashMap<Integer, int[]> myMap = new HashMap<>();
        for (int[] piece : pieces) {
            myMap.put(piece[0], piece);
        }

            while (j < repeater){
                try {
                    if (!myMap.containsKey(target[i])){
                        return false;
                    }
                }
                catch (ArrayIndexOutOfBoundsException e){
                    return false;
                }


                int[] pieceInCheck = myMap.get(target[i]);
                int num = pieceInCheck.length;


                for(int w : pieceInCheck){
                    if (w == target[i]){
                        i++;
                    }
                    else return false;
                }
                j++;
            }

        return true;
    }
}