class Solution:
    def addOperators(self, num: str, target: int) -> list[str]:
        result = []

        def backtrack(index, expression, value, prev):
            if index == len(num):
                if value == target:
                    result.append(expression)
                return

            for i in range(index, len(num)):
                # Avoid numbers with leading zeros
                if i > index and num[index] == '0':
                    break

                current = num[index:i + 1]
                current_value = int(current)

                # First number
                if index == 0:
                    backtrack(
                        i + 1,
                        current,
                        current_value,
                        current_value
                    )
                else:
                    # Addition
                    backtrack(
                        i + 1,
                        expression + "+" + current,
                        value + current_value,
                        current_value
                    )

                    # Subtraction
                    backtrack(
                        i + 1,
                        expression + "-" + current,
                        value - current_value,
                        -current_value
                    )

                    # Multiplication
                    backtrack(
                        i + 1,
                        expression + "*" + current,
                        value - prev + prev * current_value,
                        prev * current_value
                    )

        backtrack(0, "", 0, 0)

        return result
        