class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        result = set()

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

        def backtrack(index, current):
            if index == len(s):
                string = ''.join(current)

                if is_valid(string):
                    result.add(string)

                return

            ch = s[index]

            if ch == '(' or ch == ')':
                backtrack(index + 1, current)

            current.append(ch)
            backtrack(index + 1, current)
            current.pop()

        backtrack(0, [])

        max_length = max(map(len, result))

        return [string for string in result if len(string) == max_length]
        