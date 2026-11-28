class Solution(object):
    def maximumSaleItems(self, items, budget):
        """
        :type items: List[List[int]]
        :type budget: int
        :rtype: int
        """
        items.sort(key=lambda x: x[1])

        n = len(items)
        mx = max(factor for factor, price in items)

        freq = [0] * (mx + 1)

        for factor, price in items:
            freq[factor] += 1

        # Count all items having factors divisible by each factor
        for i in range(1, mx + 1):
            for j in range(i * 2, mx + 1, i):
                freq[i] += freq[j]

        min_price = items[0][1]
        ans = 0

        # Buy items that provide an additional free item
        for factor, price in items:
            if price >= 2 * min_price:
                break

            free_count = freq[factor] - 1

            take = min(free_count, budget // price)

            ans += take * 2
            budget -= take * price

        # Spend remaining budget on cheapest items
        ans += budget // min_price

        return ans
        
