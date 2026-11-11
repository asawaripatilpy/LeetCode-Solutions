class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        """
        :type cost1: int
        :type cost2: int
        :type costBoth: int
        :type need1: int
        :type need2: int
        :rtype: int
        """
        a = need1 * cost1 + need2 * cost2

        b = costBoth * max(need1, need2)

        mn = min(need1, need2)

        c = costBoth * mn + (need1 - mn) * cost1 + (need2 - mn) * cost2

        return min(a, b, c)

        
