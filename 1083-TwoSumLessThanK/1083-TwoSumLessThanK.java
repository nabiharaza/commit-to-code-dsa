// Last updated: 8/5/2025, 2:55:51 PM
class Solution {
    public int twoSumLessThanK(int[] A, int K) {
        Arrays.sort(A);
        int max=-1, i=0, j=A.length-1;
        while(i<j){
            int sum=A[i]+A[j];
            if(sum<K){
                max = Math.max(sum, max);
                ++i;
            }
            else{
                --j;
        }
    }
    return max;
}
}