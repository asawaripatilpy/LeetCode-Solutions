class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        if not matrix:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        memo = {}

        def dfs(r, c):
            if (r, c) in memo:
                return memo[(r, c)]

            longest = 1

            directions = [
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1)
            ]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (0 <= nr < rows and
                    0 <= nc < cols and
                    matrix[nr][nc] > matrix[r][c]):

                    longest = max(
                        longest,
                        1 + dfs(nr, nc)
                    )

            memo[(r, c)] = longest
            return longest

        answer = 0

        for r in range(rows):
            for c in range(cols):
                answer = max(answer, dfs(r, c))

        return answer
        