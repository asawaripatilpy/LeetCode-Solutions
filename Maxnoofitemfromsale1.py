class Solution(object):
    def maximumSaleItems(self, items, budget):
        """
        :type items: List[List[int]]
        :type budget: int
        :rtype: int
        """
        
        dp = [0] * (budget + 1)

        mn = min(price for factor, price in items)

        for factor, price in items:
            cnt = sum(
                1 for f, p in items if f % factor == 0
            )

            for j in range(budget, price - 1, -1):
                dp[j] = max(dp[j], dp[j - price] + cnt)

        ans = 0

        for i in range(budget + 1):
            ans = max(ans, dp[i] + (budget - i) // mn)

        return ans
