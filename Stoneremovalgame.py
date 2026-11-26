class Solution(object):
    def canAliceWin(self, n):
        """
        :type n: int
        :rtype: bool
        """
        stones = n
        remove = 10
        turn = 0

        while stones >= remove:
            stones -= remove
            remove -= 1
            turn += 1

        return turn % 2 == 1
        
