class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = max(nums)
        moves = 0

        for num in nums:
            moves += maximum - num

        return moves
