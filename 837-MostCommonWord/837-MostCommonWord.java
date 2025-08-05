// Last updated: 8/5/2025, 2:56:56 PM
class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        Set<String> ban = new HashSet<>(Arrays.asList(banned));
        Map<String, Integer> map = new HashMap<>();
        String[] words = paragraph.replaceAll("\\W+", " ").toLowerCase().split("\\s+");
        for (String w: words)
            if(!ban.contains(w))
                map.put(w, map.getOrDefault(w,0)+1);
        return Collections.max(map.entrySet(), Map.Entry.comparingByValue()).getKey();
    }
}