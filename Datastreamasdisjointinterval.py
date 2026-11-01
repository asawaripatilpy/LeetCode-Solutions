class SummaryRanges(object):

    def __init__(self):
        self.nums = set()
        

    def addNum(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.nums.add(value)

        

    def getIntervals(self):
        """
        :rtype: List[List[int]]
        """
        intervals = []

        for num in sorted(self.nums):
            if not intervals or num > intervals[-1][1] + 1:
                intervals.append([num, num])
            else:
                intervals[-1][1] = num

        return intervals

        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
