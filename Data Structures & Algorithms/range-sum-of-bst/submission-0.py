# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, node: Optional[TreeNode], low: int, high: int) -> int:
        sum = 0
        def dfs(root):
            nonlocal sum
            if not root: return 

            if low <= root.val <= high:
                sum += root.val
            if root.val > low:
                dfs(root.left)
            if root.val < high:     # only bother going right if there might be valid nodes there
                dfs(root.right)
        dfs(node)
        return sum
