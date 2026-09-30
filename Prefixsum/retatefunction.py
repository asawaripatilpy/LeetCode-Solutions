class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        n = len(nums)

        total = sum(nums)

        # F(0)
        f = sum(i * nums[i] for i in range(n))

        ans = f

        # F(k) = F(k-1) + total - n * nums[n-k]
        for k in range(1, n):
            f = f + total - n * nums[n - k]
            ans = max(ans, f)

        return ans
        