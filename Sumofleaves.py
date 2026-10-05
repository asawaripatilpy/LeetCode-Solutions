# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0

        total = 0

        # Check if left child is a leaf
        if root.left:
            if root.left.left is None and root.left.right is None:
                total += root.left.val
            else:
                total += self.sumOfLeftLeaves(root.left)

        # Check right subtree
        total += self.sumOfLeftLeaves(root.right)

        return total
        
