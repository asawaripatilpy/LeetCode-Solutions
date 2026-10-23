class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = max(nums)
        right = sum(nums)

        while left < right:
            mid = (left + right) // 2

            parts = 1
            current_sum = 0

            for num in nums:
                if current_sum + num > mid:
                    parts += 1
                    current_sum = num
                else:
                    current_sum += num

            if parts > k:
                left = mid + 1
            else:
                right = mid

        return left

        
