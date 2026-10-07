class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
    
        
        def is_valid(string):
            count = 0

            for ch in string:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1

                    if count < 0:
                        return False

            return count == 0

        queue = {s}

        while queue:
            valid = []

            # Current level मधील strings check करा
            for string in queue:
                if is_valid(string):
                    valid.append(string)

            # Valid strings मिळाल्या म्हणजे minimum removals झाले
            if valid:
                return valid

            next_level = set()

            # प्रत्येक string मधून एक parenthesis remove करा
            for string in queue:
                for i in range(len(string)):
                    if string[i] in "()":
                        new_string = string[:i] + string[i + 1:]
                        next_level.add(new_string)

            queue = next_level

        return [""]
        
