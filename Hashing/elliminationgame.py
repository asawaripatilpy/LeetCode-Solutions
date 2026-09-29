class Solution:
    def lastRemaining(self, n: int) -> int:
        head = 1
        step = 1
        remaining = n
        left = True

        while remaining > 1:
            # If eliminating from left,
            # or if number of elements is odd,
            # the head moves forward.
            if left or remaining % 2 == 1:
                head += step

            remaining //= 2
            step *= 2
            left = not left

        return head
        