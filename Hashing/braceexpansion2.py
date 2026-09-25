class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def dfs(i):
            result = set()
            current = {""}

            while i < len(expression) and expression[i] != '}':
                if expression[i] == '{':
                    nxt, i = dfs(i + 1)

                elif expression[i] == ',':
                    result |= current
                    current = {""}
                    i += 1
                    continue

                else:
                    nxt = {expression[i]}
                    i += 1

                # Concatenation
                current = {a + b for a in current for b in nxt}

            result |= current

            return result, i + 1

        result, _ = dfs(0)

        return sorted(result)
        