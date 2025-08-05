// Last updated: 8/5/2025, 2:56:03 PM
class Solution {
    public int[][] intervalIntersection(int[][] A, int[][] B) {
        if (A == null || B == null || A.length == 0 || B.length == 0)
            return new int[][]{};
        List<int[]> res = new LinkedList<>();
        int i=0, j=0;
        int startMax, endMin;
        while(i < A.length && j < B.length){
            startMax = Math.max(A[i][0], B[j][0]);
            endMin = Math.min(A[i][1], B[j][1]);
            
            if (endMin >= startMax)
                res.add(new int[]{startMax, endMin});
            
            if (A[i][1] == endMin)
                i++;
            if (B[j][1] == endMin)
                j++;
        }
        return res.toArray(new int[res.size()][2]);
    }
}