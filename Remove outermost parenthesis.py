class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        balance = 0
        
        for char in s:
            if char == '(':
                if balance > 0:
                    result.append(char)
                balance += 1
            else:
                balance -= 1
                if balance > 0:
                    result.append(char)
                    
        return "".join(result)
    
