class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [1]

        indices = [0] * len(primes)

        values = primes[:]

        for _ in range(1, n):
            next_ugly = min(values)
            ugly.append(next_ugly)

            for i in range(len(primes)):
                if values[i] == next_ugly:
                    indices[i] += 1
                    values[i] = ugly[indices[i]] * primes[i]

        return ugly[-1]
        