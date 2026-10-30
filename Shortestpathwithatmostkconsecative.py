class Solution(object):
    def shortestPath(self, n, edges, labels, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :type k: int
        :rtype: int
        """
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        if n == 1:
            return 0

        INF = float('inf')
        dist = [[INF] * (k + 1) for _ in range(n)]

        count = 1
        dist[0][1] = 0

        pq = [(0, 0, count)]

        while pq:
            d, u, cnt = heapq.heappop(pq)

            if d != dist[u][cnt]:
                continue

            if u == n - 1:
                return d

            for v, w in graph[u]:
                if labels[v] == labels[u]:
                    new_cnt = cnt + 1
                else:
                    new_cnt = 1

                if new_cnt > k:
                    continue

                new_dist = d + w

                if new_dist < dist[v][new_cnt]:
                    dist[v][new_cnt] = new_dist
                    heapq.heappush(
                        pq, (new_dist, v, new_cnt)
                    )

        return -1
        
