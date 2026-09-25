class Solution:
    def superPow(self, a: int, b: list[int]) -> int:
        MOD = 1337

        def power(a, n):
            result = 1

            while n > 0:
                if n % 2 == 1:
                    result = (result * a) % MOD

                a = (a * a) % MOD
                n //= 2

            return result

        result = 1

        for digit in b:
            result = (power(result, 10) * power(a, digit)) % MOD

        return result
        