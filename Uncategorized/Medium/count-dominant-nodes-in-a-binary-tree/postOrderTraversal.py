# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:
        count = 0

        def dfs(node: TreeNode | None) -> float:
            nonlocal count
            if not node:
                return float('-inf')
            
            left_max = dfs(node.left)
            right_max = dfs(node.right)
            curr_max = max(node.val, left_max, right_max)
            
            if node.val == curr_max:
                count += 1
                
            return curr_max

        dfs(root)
        return count