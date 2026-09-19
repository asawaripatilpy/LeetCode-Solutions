class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        n = len(nums)

        mid = (n + 1) // 2

        small = nums[:mid][::-1]
        large = nums[mid:][::-1]

        nums[::2] = small
        nums[1::2] = large
        