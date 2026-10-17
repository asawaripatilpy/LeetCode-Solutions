class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        length = 0
        odd_found = False

        for freq in count.values():
            length += (freq // 2) * 2

            if freq % 2 == 1:
                odd_found = True

        if odd_found:
            length += 1

        return length
