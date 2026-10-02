# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        prefix = {0: 1}

        def dfs(node, current_sum):
            if not node:
                return 0

            current_sum += node.val

            # Number of paths whose sum is targetSum
            count = prefix.get(current_sum - targetSum, 0)

            # Add current sum to prefix map
            prefix[current_sum] = prefix.get(current_sum, 0) + 1

            count += dfs(node.left, current_sum)
            count += dfs(node.right, current_sum)

            # Remove current path's sum while backtracking
            prefix[current_sum] -= 1

            return count

        return dfs(root, 0)
        