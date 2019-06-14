# String

# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.
#
# Example 1:
#
# Input: "3+2*2"
# Output: 7
# Example 2:
#
# Input: " 3/2 "
# Output: 1
# Example 3:
#
# Input: " 3+5 / 2 "
# Output: 5
# Note:
#
# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.

class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def nextInt(s, i):
            res = 0
            while i<len(s) and s[i] not in "+-*/":
                res=res*10+ord(s[i])-ord('0')
                i+=1
            return (res, i)

        s = s.replace(" ", "")
        stack = []
        i = 0
        tmp, i = nextInt(s, 0)
        stack.append(tmp)
        while i < len(s):
            op=s[i]
            tmp, i = nextInt(s, i+1)
            if op == "+":
                stack.append(tmp)
            elif op == "-":
                stack.append(-tmp)
            elif op == "*":
                stack[-1]*=tmp
            elif op == "/":
                stack[-1] = stack[-1] // tmp if stack[-1]>=0 else -((-stack[-1])//tmp)
        return sum(stack)
