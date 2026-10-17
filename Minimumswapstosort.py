class Solution(object):
    def minSwaps(self, nums):
        """"""
        def digit_sum(num):
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            return total

        arr = sorted(nums, key=lambda num: (digit_sum(num), num))
        n = len(nums)

        position = {value: i for i, value in enumerate(arr)}
        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i]:
                continue

            j = i
            cycle_size = 0

            while not visited[j]:
                visited[j] = True
                j = position[nums[j]]
                cycle_size += 1

            if cycle_size > 1:
                swaps += cycle_size - 1

        return swaps

        
        
        
