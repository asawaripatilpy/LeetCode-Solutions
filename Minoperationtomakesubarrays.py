class Solution(object):
    def minOperations(self, nums, x, k):
        """
        :type nums: List[int]
        :type x: int
        :type k: int
        :rtype: int
        """
        n = len(nums)

        vals = sorted(set(nums))
        m = len(vals)

        rank = {v: i + 1 for i, v in enumerate(vals)}

        count_tree = [0] * (m + 1)
        sum_tree = [0] * (m + 1)

        def add(tree, idx, val):
            while idx <= m:
                tree[idx] += val
                idx += idx & -idx

        def query(tree, idx):
            res = 0
            while idx > 0:
                res += tree[idx]
                idx -= idx & -idx
            return res

        def kth(k):
            idx = 0
            bit = 1 << (m.bit_length() - 1)

            while bit:
                nxt = idx + bit

                if nxt <= m and count_tree[nxt] < k:
                    idx = nxt
                    k -= count_tree[nxt]

                bit >>= 1

            return idx + 1

        total = 0
        costs = []

        for i in range(x):
            v = nums[i]
            idx = rank[v]

            add(count_tree, idx, 1)
            add(sum_tree, idx, v)

            total += v

        def get_cost():
            median_idx = kth((x + 1) // 2)
            median = vals[median_idx - 1]

            left_count = query(count_tree, median_idx)
            left_sum = query(sum_tree, median_idx)

            right_count = x - left_count
            right_sum = total - left_sum

            return (
                median * left_count - left_sum
                + right_sum - median * right_count
            )

        costs.append(get_cost())

        for i in range(x, n):
            old = nums[i - x]
            idx = rank[old]

            add(count_tree, idx, -1)
            add(sum_tree, idx, -old)

            total -= old

            new = nums[i]
            idx = rank[new]

            add(count_tree, idx, 1)
            add(sum_tree, idx, new)

            total += new

            costs.append(get_cost())

        INF = 10**18

        dp = [0] * (n + 1)

        for t in range(1, k + 1):
            new_dp = [INF] * (n + 1)

            for i in range(x, n + 1):
                new_dp[i] = new_dp[i - 1]

                start = i - x

                new_dp[i] = min(
                    new_dp[i],
                    dp[start] + costs[start]
                )

            dp = new_dp

        return dp[n]

                        
