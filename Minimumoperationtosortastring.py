class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)

        # Case 1: Already sorted
        if s == ''.join(sorted(s)):
            return 0

        # Case 2: Cannot sort a reversed string of length 2
        if n == 2:
            return -1

        mn = min(s)
        mx = max(s)

        # Case 3: Minimum at start or maximum at end
        if s[0] == mn or s[-1] == mx:
            return 1

        # Case 4: Minimum or maximum in the middle
        if mn in s[1:-1] or mx in s[1:-1]:
            return 2

        # Case 5: Otherwise
        return 3

        
