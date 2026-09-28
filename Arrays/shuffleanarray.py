class Solution:

    def __init__(self, nums: list[int]):
        self.original = nums[:]

        

    def reset(self) -> list[int]:
        return self.original[:]
        

    def shuffle(self) -> list[int]:
        shuffled = self.original[:]
        random.shuffle(shuffled)
        return shuffled
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()