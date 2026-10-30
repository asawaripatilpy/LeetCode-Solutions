class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        
        stack = [0]
        max_len = 0

        for line in input.split('\n'):
            depth = line.count('\t')
            name = line.lstrip('\t')

            while len(stack) > depth + 1:
                stack.pop()

            current_len = stack[-1] + len(name)

            if '.' in name:
                max_len = max(max_len, current_len)
            else:
                stack.append(current_len + 1)

        return max_len
