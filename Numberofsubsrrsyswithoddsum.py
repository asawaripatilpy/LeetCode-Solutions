class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7

        odd = 0
        even = 1
        prefix_sum = 0
        result = 0

        for num in arr:
            prefix_sum += num

            if prefix_sum % 2 == 1:
                result += even
                odd += 1
            else:
                result += odd
                even += 1

        return result % MOD
        
