# Greedy

# Given two integers A and B, return any string S such that:
#
# S has length A + B and contains exactly A 'a' letters, and exactly B 'b' letters;
# The substring 'aaa' does not occur in S;
# The substring 'bbb' does not occur in S.
#
#
# Example 1:
#
# Input: A = 1, B = 2
# Output: "abb"
# Explanation: "abb", "bab" and "bba" are all correct answers.
# Example 2:
#
# Input: A = 4, B = 1
# Output: "aabaa"
#
#
# Note:
#
# 0 <= A <= 100
# 0 <= B <= 100
# It is guaranteed such an S exists for the given A and B.

class Solution(object):
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        if A - B >= 2:
            res = "aa"
            A -= 2
        elif B - A >= 2:
            res = "bb"
            B -= 2
        elif A == B:
            return "ab" * A
        elif A > B:
            return "a" + "ba" * B
        else:
            return "b" + "ab" * A

        while A > 0 or B > 0:
            prev = res[-1]
            if A == B:
                if prev == 'a':
                    return res + "ba" * A
                else:
                    return res + "ab" * A
            elif prev == 'a':
                if B - A >= 2:
                    res += "bb"
                    B -= 2
                elif B - A == 1:
                    return res + "b" + "ab" * A
                else:
                    res += "b"
                    B -= 1
            elif prev == 'b':
                if A - B >= 2:
                    res += "aa"
                    A -= 2
                elif A - B == 1:
                    return res + "a" + "ba" * B
                else:
                    res += "a"
                    A -= 1
        return res
