class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.indices = {}

        for i, num in enumerate(nums):
            if num not in self.indices:
                self.indices[num] = []
            self.indices[num].append(i)
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        
        return random.choice(self.indices[target])
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
