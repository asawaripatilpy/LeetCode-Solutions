class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        
        count = 0

        for num1 in arr1:
            valid = True

            for num2 in arr2:
                if abs(num1 - num2) <= d:
                    valid = False
                    break

            if valid:
                count += 1

        return count
