class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)

        tree = [[0, 0] for _ in range(4 * n)]
        lazy = [0] * (4 * n)

        def push(node, l, r):
            if lazy[node] == 0 or l == r:
                return

            mid = (l + r) // 2
            for child, length in (
                (node * 2, mid - l + 1),
                (node * 2 + 1, r - mid)
            ):
                d = lazy[node]
                s = tree[child][0]
                tree[child][1] = (
                    tree[child][1] + 2 * d * s + d * d * length
                ) % MOD
                tree[child][0] = (s + d * length) % MOD
                lazy[child] += d

            lazy[node] = 0

        def update(node, l, r, ql, qr, val):
            if ql > r or qr < l:
                return

            if ql <= l and r <= qr:
                length = r - l + 1
                s = tree[node][0]
                tree[node][1] = (
                    tree[node][1] + 2 * val * s
                    + val * val * length
                ) % MOD
                tree[node][0] = (s + val * length) % MOD
                lazy[node] += val
                return

            push(node, l, r)
            mid = (l + r) // 2

            update(node * 2, l, mid, ql, qr, val)
            update(node * 2 + 1, mid + 1, r, ql, qr, val)

            tree[node][0] = (
                tree[node * 2][0] + tree[node * 2 + 1][0]
            ) % MOD
            tree[node][1] = (
                tree[node * 2][1] + tree[node * 2 + 1][1]
            ) % MOD

        last = {}
        ans = 0

        for i, x in enumerate(nums):
            left = last.get(x, -1) + 1
            update(1, 0, n - 1, left, i, 1)
            last[x] = i
            ans = (ans + tree[1][1]) % MOD

        return ans
        
        
