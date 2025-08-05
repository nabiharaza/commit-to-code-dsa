// Last updated: 8/5/2025, 2:53:58 PM
class Solution {
    public String arrangeWords(String text) {
        if(text == null || text.length() == 0) return text;
        String[] arr = text.split(" ");
        char c = Character.toLowerCase(arr[0].charAt(0));
        arr[0] = String.valueOf(c).concat(arr[0].substring(1));
        
        Comparator<String> cmp = new Comparator<String>(){
            @Override
            public int compare(String s1, String s2){
                int l1 = s1.length();
                int l2 = s2.length();
                return Integer.compare(l1,l2);
            }
        };
        Arrays.sort(arr, cmp);
        c = Character.toUpperCase(arr[0].charAt(0));
        arr[0] = String.valueOf(c).concat(arr[0].substring(1));
        StringBuilder sb = new StringBuilder();
        for(String s: arr){
            sb.append(" ");
            sb.append(s);
        }
        return sb.toString().trim();
    }
}