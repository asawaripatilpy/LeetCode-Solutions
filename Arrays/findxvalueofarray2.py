class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)

        # tree[node] = [product_mod_k, count_of_prefix_products]
        tree = [(1 % k, [0] * k) for _ in range(4 * n)]

        def merge(left, right):
            left_prod, left_cnt = left
            right_prod, right_cnt = right

            prod = (left_prod * right_prod) % k

            cnt = left_cnt[:]

            for r in range(k):
                new_rem = (left_prod * r) % k
                cnt[new_rem] += right_cnt[r]

            return (prod, cnt)

        def build(node, l, r):
            if l == r:
                rem = nums[l] % k

                cnt = [0] * k
                cnt[rem] = 1

                tree[node] = (rem, cnt)
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, l, r, index, value):
            if l == r:
                rem = value % k

                cnt = [0] * k
                cnt[rem] = 1

                tree[node] = (rem, cnt)
                return

            mid = (l + r) // 2

            if index <= mid:
                update(node * 2, l, mid, index, value)
            else:
                update(node * 2 + 1, mid + 1, r, index, value)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def query(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return tree[node]

            mid = (l + r) // 2

            if qr <= mid:
                return query(node * 2, l, mid, ql, qr)

            if ql > mid:
                return query(node * 2 + 1, mid + 1, r, ql, qr)

            left = query(node * 2, l, mid, ql, qr)
            right = query(node * 2 + 1, mid + 1, r, ql, qr)

            return merge(left, right)

        build(1, 0, n - 1)

        answer = []

        for index, value, start, x in queries:

            # Persistent update
            update(1, 0, n - 1, index, value)

            # Query nums[start ... n-1]
            result = query(1, 0, n - 1, start, n - 1)

            answer.append(result[1][x])

        return answer
