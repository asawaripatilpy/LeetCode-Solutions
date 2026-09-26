class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        # Create dictionary from knowledge
        knowledge_dict = dict(knowledge)

        result = []
        i = 0

        while i < len(s):
            if s[i] == '(':
                j = i + 1

                # Find closing bracket
                while s[j] != ')':
                    j += 1

                key = s[i + 1:j]

                # Get value or '?' if key doesn't exist
                result.append(knowledge_dict.get(key, '?'))

                i = j + 1
            else:
                result.append(s[i])
                i += 1

        return ''.join(result)
        