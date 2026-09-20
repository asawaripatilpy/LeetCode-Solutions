class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0

        for i, ch in enumerate(s):
            value = ord(ch) - ord('a') + 1
            reverse_value = 27 - value
            total += reverse_value * (i + 1)

        return total
        