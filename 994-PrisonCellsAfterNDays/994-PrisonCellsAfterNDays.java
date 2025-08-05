// Last updated: 8/5/2025, 2:56:15 PM
class Solution {
    public int[] prisonAfterNDays(int[] cells, int n) {
        HashSet<String> set = new HashSet<>();
        int count = 0;
        for (int i=0; i<n; i++) {
            int[] nextDay = findNext(cells);
            String key = Arrays.toString(nextDay);
            if(!set.contains(key)) {
                set.add(key);
                count++;
            }
            else {
                break;
            }
            cells = nextDay;
        }

        n%=count;
        for(int i=0; i<n; i++) {
            cells = findNext(cells);
        }
        return cells;

    }

    public int[] findNext(int[] cells) {
        int[] nextCells = new int[cells.length];
        for(int i=1; i<cells.length-1; i++) 
            nextCells[i] = cells[i-1] == cells[i+1] ? 1 : 0;
        return nextCells;
    }
}