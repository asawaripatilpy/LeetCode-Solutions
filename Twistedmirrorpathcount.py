class Solution(object):
    def uniquePaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7

        m, n = len(grid), len(grid[0])

        dp = [1] + [0] * (n - 1)

        for i in range(m):
            right = 0

            for j in range(n):
                if grid[i][j] == 1:
                    right, dp[j] = dp[j], right
                else:
                    right = (right + dp[j]) % MOD
                    dp[j] = right

        return right
        
