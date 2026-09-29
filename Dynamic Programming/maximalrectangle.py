class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        heights = [0] * cols
        max_area = 0

        for row in matrix:
            # Build histogram heights
            for j in range(cols):
                if row[j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0

            # Find largest rectangle in histogram
            stack = [-1]

            for j in range(cols):
                while stack[-1] != -1 and heights[stack[-1]] >= heights[j]:
                    h = heights[stack.pop()]
                    width = j - stack[-1] - 1
                    max_area = max(max_area, h * width)

                stack.append(j)

            # Process remaining bars
            while stack[-1] != -1:
                h = heights[stack.pop()]
                width = cols - stack[-1] - 1
                max_area = max(max_area, h * width)

        return max_area

        