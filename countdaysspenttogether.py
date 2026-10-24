
class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        months = [31, 28, 31, 30, 31, 30,
                  31, 31, 30, 31, 30, 31]

        def days(date):
            month, day = map(int, date.split("-"))
            return sum(months[:month - 1]) + day

        start = max(days(arriveAlice), days(arriveBob))
        end = min(days(leaveAlice), days(leaveBob))

        return max(0, end - start + 1)
        
