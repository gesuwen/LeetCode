# Given an integer, return its base 7 string representation.
#
# Example 1:
# Input: 100
# Output: "202"
# Example 2:
# Input: -7
# Output: "-10"
# Note: The input will be in range of [-1e7, 1e7].

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        numStr = str(num)
        if numStr[0] == "-":
            numPart = int(numStr[1:])
        else:
            numPart = num
        dig = 0
        output = []
        while 7*7**dig <= numPart:
            dig += 1
        for i in range(dig, -1, -1):
            for j in range(6, -1, -1):
                if j*7**i <= numPart:
                    numPart -= j*7**i
                    output.append(j)
                    break
        if num < 0:
            return "-" + "".join(map(str, output))
        return "".join(map(str, output))
            
