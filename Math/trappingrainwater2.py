class Solution:
    def trapRainWater(self, heightMap: list[list[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        m = len(heightMap)
        n = len(heightMap[0])

        heap = []
        visited = [[False] * n for _ in range(m)]

        # Add boundary cells
        for i in range(m):
            heapq.heappush(heap, (heightMap[i][0], i, 0))
            heapq.heappush(heap, (heightMap[i][n - 1], i, n - 1))
            visited[i][0] = True
            visited[i][n - 1] = True

        for j in range(n):
            heapq.heappush(heap, (heightMap[0][j], 0, j))
            heapq.heappush(heap, (heightMap[m - 1][j], m - 1, j))
            visited[0][j] = True
            visited[m - 1][j] = True

        water = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while heap:
            height, r, c = heapq.heappop(heap)

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True

                    new_height = max(height, heightMap[nr][nc])

                    if height > heightMap[nr][nc]:
                        water += height - heightMap[nr][nc]

                    heapq.heappush(heap, (new_height, nr, nc))

        return water
        