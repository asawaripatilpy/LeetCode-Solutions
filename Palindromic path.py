class Solution(object):
    def palindromePath(self, n, edges, s, queries):
        """
        :type n: int
        :type edges: List[List[int]]
        :type s: str
        :type queries: List[str]
        :rtype: List[bool]
        """
        from collections import defaultdict

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        size = [1] * n
        heavy = [-1] * n

        order = [0]
        for u in order:
            for v in adj[u]:
                if v == parent[u]:
                    continue
                parent[v] = u
                depth[v] = depth[u] + 1
                order.append(v)

        for u in reversed(order):
            largest = 0
            for v in adj[u]:
                if parent[v] == u:
                    size[u] += size[v]
                    if size[v] > largest:
                        largest = size[v]
                        heavy[u] = v

        head = [0] * n
        pos = [0] * n
        timer = 0
        stack = [(0, 0)]

        while stack:
            u, h = stack.pop()
            while u != -1:
                head[u] = h
                pos[u] = timer
                timer += 1

                for v in adj[u]:
                    if parent[v] == u and v != heavy[u]:
                        stack.append((v, v))

                u = heavy[u]

        size_tree = 1
        while size_tree < n:
            size_tree *= 2

        tree = [0] * (2 * size_tree)

        for u in range(n):
            tree[size_tree + pos[u]] = 1 << (ord(s[u]) - ord('a'))

        for i in range(size_tree - 1, 0, -1):
            tree[i] = tree[2 * i] ^ tree[2 * i + 1]

        def update(p, value):
            p += size_tree
            tree[p] = value
            p //= 2

            while p:
                tree[p] = tree[2 * p] ^ tree[2 * p + 1]
                p //= 2
        def range_query(l, r):
            result = 0
            l += size_tree
            r += size_tree + 1

            while l < r:
                if l & 1:
                    result ^= tree[l]
                    l += 1
                if r & 1:
                    r -= 1
                    result ^= tree[r]

                l //= 2
                r //= 2

            return result

        def path_query(u, v):
            mask = 0

            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u

                mask ^= range_query(pos[head[u]], pos[u])
                u = parent[head[u]]

            if depth[u] > depth[v]:
                u, v = v, u

            mask ^= range_query(pos[u], pos[v])
            return mask

        chars = list(s)
        answer = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                chars[u] = c
                update(pos[u], 1 << (ord(c) - ord('a')))

            else:
                u = int(parts[1])
                v = int(parts[2])
                mask = path_query(u, v)
                answer.append((mask & (mask - 1)) == 0)

        return answer

                    
