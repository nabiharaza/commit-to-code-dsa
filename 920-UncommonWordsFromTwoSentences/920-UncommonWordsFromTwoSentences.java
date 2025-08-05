// Last updated: 8/5/2025, 2:56:34 PM
class Solution {
    public String[] uncommonFromSentences(String A, String B) {
        Map<String, Integer> count = new HashMap<>();
        for(String word: (A + " " + B).split(" "))
            count.put(word, count.getOrDefault(word, 0) +1);
        ArrayList<String> result = new ArrayList<>();
        for(String word: count.keySet())
            if(count.get(word) == 1)
                result.add(word);
    return result.toArray(new String[0]);
    }
}