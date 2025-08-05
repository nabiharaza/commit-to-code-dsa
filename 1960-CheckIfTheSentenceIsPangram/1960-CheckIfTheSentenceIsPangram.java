// Last updated: 8/5/2025, 2:52:46 PM
class Solution {
    public boolean checkIfPangram(String sentence) {
        HashSet<Character> set = new HashSet<>();
        for(Character c : sentence.toLowerCase().toCharArray())
            set.add(c);
        
        return set.size() == 26;
    }
}