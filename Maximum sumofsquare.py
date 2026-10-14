class Solution(object):
    def maxSumOfSquares(self, num, sum):
        """
        :type num: int
        :type sum: int
        :rtype: str
        """
        if sum > 9 * num:
            return ""

        k, r = divmod(sum, 9)

        ans = "9" * k

        if r > 0:
            ans += str(r)

        ans += "0" * (num - len(ans))

        return ans

    
