class Solution(object):
    def minimumChanges(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)

        cost = [[0] * (n + 1) for _ in range(n)]

        # Step 1: Calculate minimum changes for every substring
        for l in range(n):
            for r in range(l + 2, n + 1):
                length = r - l
                best = float('inf')

                for d in range(1, length):
                    if length % d != 0:
                        continue

                    groups = length // d
                    changes = 0

                    for i in range(d):
                        for j in range(groups // 2):
                            left = l + i + j * d
                            right = l + i + (groups - 1 - j) * d

                            if s[left] != s[right]:
                                changes += 1

                    best = min(best, changes)

                cost[l][r] = best

        # Step 2: Dynamic Programming
        dp = [[float('inf')] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for parts in range(1, k + 1):
            for end in range(2 * parts, n + 1):
                for start in range(2 * (parts - 1), end - 1):
                    dp[parts][end] = min(
                        dp[parts][end],
                        dp[parts - 1][start] + cost[start][end]
                    )

        return dp[k][n]

                
        
        
