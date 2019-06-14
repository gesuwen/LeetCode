# Math

# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
#
# Note:
#
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.
class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1List, num2List = list(num1), list(num2)
        prev = 0
        output = []
        while num1List or num2List:
            if num1List and num2List:
                curr = int(num1List.pop()) + int(num2List.pop()) + prev
                prev = 0
                currStr = str(curr)
                output = [currStr[-1]] + output
                if len(currStr) > 1:
                    prev = int(currStr[:-1])
            elif num1List:
                curr = int(num1List.pop()) + prev
                prev = 0
                currStr = str(curr)
                output = [currStr[-1]] + output
                if len(currStr) > 1:
                    prev = int(currStr[:-1])
            elif num2List:
                curr = int(num2List.pop()) + prev
                prev = 0
                currStr = str(curr)
                output = [currStr[-1]] + output
                if len(currStr) > 1:
                    prev = int(currStr[:-1])
        if prev != 0:
            output = [str(prev)] + output
        output = ''.join(output)
        return output
