class Solution(object):
    def countServers(self, n, logs, x, queries):
        """
        :type n: int
        :type logs: List[List[int]]
        :type x: int
        :type queries: List[int]
        :rtype: List[int]
        """
        logs.sort(key=lambda log: log[1])

        queries_sorted = sorted(enumerate(queries), key=lambda q: q[1])

        result = [0] * len(queries)
        active = {}
        left = 0
        right = 0

        for idx, q in queries_sorted:
            while right < len(logs) and logs[right][1] <= q:
                server = logs[right][0]
                active[server] = active.get(server, 0) + 1
                right += 1

            while left < right and logs[left][1] < q - x:
                server = logs[left][0]
                active[server] -= 1

                if active[server] == 0:
                    del active[server]

                left += 1

            result[idx] = n - len(active)

        return result
