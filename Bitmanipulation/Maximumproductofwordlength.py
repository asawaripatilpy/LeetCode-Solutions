class Solution:
    def maxProduct(self, words: list[str]) -> int:
        n = len(words)
        masks = []

        for word in words:
            mask = 0

            for ch in word:
                mask |= 1 << (ord(ch) - ord('a'))

            masks.append(mask)

        max_product = 0

        for i in range(n):
            for j in range(i + 1, n):
                if masks[i] & masks[j] == 0:
                    product = len(words[i]) * len(words[j])
                    max_product = max(max_product, product)

        return max_product
        