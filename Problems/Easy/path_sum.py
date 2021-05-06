# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        if root.val == targetSum:
            if not root.left and not root.right:
                return True
        val = targetSum - root.val
        return self.hasPathSum(root.right, val) or self.hasPathSum(root.left, val)


root = TreeNode(1)
a = TreeNode(-2)
b = TreeNode(-3)
c = TreeNode(1)
d = TreeNode(3)
e = TreeNode(-2)
f = TreeNode(-1)

root.left = a
root.right = b
root.left.left = c
root.left.right = d
root.right.left = e
root.left.left.left = f

sol = Solution()
sol.hasPathSum(root, -1)
