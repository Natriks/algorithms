# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root:
            if root.left and not root.right:
                return self.minDepth(root.left) + 1
            elif not root.left and root.right:
                return self.minDepth(root.right) + 1
            else:
                left_depth = self.minDepth(root.left)
                right_depth = self.minDepth(root.right)
            return min(left_depth, right_depth) + 1
        else:
            return 0
