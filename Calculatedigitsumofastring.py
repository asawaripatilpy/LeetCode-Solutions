class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        while len(s) > k:
            res = ""
            for i in range(0, len(s), k):
                group = s[i:i + k]
                total = sum(int(digit) for digit in group)
                res += str(total)
            s = res

        return s 
        
