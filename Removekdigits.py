class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        
        for digit in num:
            # Drop larger previous digits to make the left numbers as small as possible
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
            
        # If k > 0, remove the remaining digits from the right end
        if k > 0:
            stack = stack[:-k]
            
        # Join into string and strip leading zeros
        result = "".join(stack).lstrip("0")
        
        # If the result is empty, return "0"
        return result if result else "0"
        
