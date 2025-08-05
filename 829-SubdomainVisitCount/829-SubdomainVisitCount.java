// Last updated: 8/5/2025, 2:56:59 PM
class Solution {
    public List<String> subdomainVisits(String[] cpdomains) {
        
        Map<String, Integer> map = new HashMap<>();
        for(String cd: cpdomains) {
            
            int i = cd.indexOf(' ');
            int n = Integer.parseInt(cd.substring(0,  i));
            String s = cd.substring(i+1);
            map.put(s, map.getOrDefault(s,0)+n);
            
            for(i =0; i<s.length(); i++) {
                if(s.charAt(i) == '.') {
                    String d = s.substring(i+1);
                    map.put(d, map.getOrDefault(d,0)+n);
                }
            }
            
        }
        List<String> res = new LinkedList<>();
        for(String str: map.keySet())
            res.add(map.get(str)+" "+str);
        return res;
        
    }
}