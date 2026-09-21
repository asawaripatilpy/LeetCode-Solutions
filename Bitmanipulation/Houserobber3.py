# Definiaode:
                return (0, 0)

            left = dfs(node.left)
            right = dfs(node.right)

            # Rob current house
            rob_current = node.val + left[1] + right[1]

            # Skip current house
            skip_current = max(left) + max(right)

            return (rob_current, skip_current)

        return max(dfs(root))
        