# String

# Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.
# Example 1:
# Input: ["23:59","00:00"]
# Output: 1
# Note:
# The number of time points in the given list is at least 2 and won't exceed 20000.
# The input time is legal and ranges from 00:00 to 23:59.

class Solution:
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        timeDiff = []
        for x in timePoints:
            timeDiff.append(int(x[:2])*60 + int(x[3:]))
        timeDiff.append(24*60 + min(timeDiff))
        timeDiff.sort()
        diffList = [x - timeDiff[i - 1] for i, x in enumerate(timeDiff)][1:]
        return min(diffList)
