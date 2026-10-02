class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        # Find a character whose frequency is less than k
        for ch in count:
            if count[ch] < k:
                # Split string around this invalid character
                parts = s.split(ch)

                # Solve each part separately
                return max(
                    self.longestSubstring(part, k)
                    for part in parts
                )

        # Every character appears at least k times
        return len(s)
        