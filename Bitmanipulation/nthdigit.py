class Solution:
    def findNthDigit(self, n: int) -> int:
        digit_length = 1
        count = 9
        start = 1

        # Find which group contains n
        while n > digit_length * count:
            n -= digit_length * count
            digit_length += 1
            count *= 10
            start *= 10

        # Find the actual number
        number = start + (n - 1) // digit_length

        # Find the digit inside that number
        digit_index = (n - 1) % digit_length

        return int(str(number)[digit_index])
        