class Solution(object):
    def sortPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = -1

        for i, x in enumerate(nums):
            if i != x:
                ans &= x

        return max(ans, 0)

        
