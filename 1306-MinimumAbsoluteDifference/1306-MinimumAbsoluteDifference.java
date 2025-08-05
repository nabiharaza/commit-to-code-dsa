// Last updated: 8/5/2025, 2:54:39 PM
class Solution {
    public List<List<Integer>> minimumAbsDifference(int[] arr) {
        Arrays.sort(arr);
        int min = Integer.MAX_VALUE;
        List<List<Integer>> result = new ArrayList<>();
        for(int i=0; i<arr.length-1; i++){
            int diff = arr[i+1] - arr[i];
            if(diff < min){
                min = diff;
                result.clear();
                result.add(Arrays.asList(arr[i], arr[i+1]));
            } else if (diff == min){
                result.add(Arrays.asList(arr[i], arr[i+1]));
            }
        }
        return result;
    }
}