class Solution(object):
    def maxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 0

        for i in range(n):
            prod = 1
            gcd_val = 0
            lcm_val = 1

            for j in range(i, n):
                x = nums[j]

                prod *= x

                # Calculate GCD
                a, b = gcd_val, x
                while b:
                    a, b = b, a % b
                gcd_val = a

                # Calculate LCM
                lcm_val = lcm_val * x // self.gcd(lcm_val, x)

                if prod == gcd_val * lcm_val:
                    ans = max(ans, j - i + 1)

        return ans

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
