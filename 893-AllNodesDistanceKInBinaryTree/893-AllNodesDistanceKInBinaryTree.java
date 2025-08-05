// Last updated: 8/5/2025, 2:56:46 PM
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public List<Integer> distanceK(TreeNode root, TreeNode target, int K) {
        HashMap<TreeNode, List<TreeNode>> map = new HashMap<TreeNode, List<TreeNode>>();
        buildMap(map, root, null);
        Set<TreeNode> visited = new HashSet<>();
        Queue<TreeNode> queue = new LinkedList<>();
        
        queue.offer(target);
        visited.add(target);
        
        while(!queue.isEmpty() && K-- > 0) {
            int size = queue.size();
            for(int i=0; i< size; i++) {
                TreeNode node = queue.poll();
                for(TreeNode next: map.get(node))
                    if(visited.add(next))   
                        queue.offer(next);
            }
        }
        List<Integer> res = new LinkedList<>();
        for(TreeNode node: queue)
            res.add(node.val);
        return res;
        
    }
    
    private void buildMap(Map<TreeNode, List<TreeNode>> map, TreeNode node, TreeNode parent) {
        if(node == null) return;
        if(!map.containsKey(node)) {
            map.put(node, new LinkedList<TreeNode>());
            if(parent!=null) {
                map.get(node).add(parent);
                map.get(parent).add(node);
            }
            buildMap(map, node.left, node);
            buildMap(map, node.right, node);
        }
    }
    
}