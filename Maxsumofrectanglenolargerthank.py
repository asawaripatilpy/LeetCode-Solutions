class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        rows, cols = len(matrix), len(matrix[0])
        ans = float('-inf')

        # Keep the number of rows smaller when possible
        if rows > cols:
            matrix = [list(row) for row in zip(*matrix)]
            rows, cols = cols, rows

        for left in range(cols):
            sums = [0] * rows

            for right in range(left, cols):
                for r in range(rows):
                    sums[r] += matrix[r][right]

                # Maximum subarray sum <= k
                prefix = 0
                sorted_prefix = [0]

                for value in sums:
                    prefix += value

                    # Find smallest previous prefix >= prefix - k
                    i = bisect_left(sorted_prefix, prefix - k)

                    if i < len(sorted_prefix):
                        ans = max(ans, prefix - sorted_prefix[i])

                    insort(sorted_prefix, prefix)

                    if ans == k:
                        return k

        return ans

        
