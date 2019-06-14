# Greedy

# Given a non-negative integer N, find the largest number that is less than or equal to N with monotone increasing digits.
#
# (Recall that an integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.)
#
# Example 1:
# Input: N = 10
# Output: 9
# Example 2:
# Input: N = 1234
# Output: 1234
# Example 3:
# Input: N = 332
# Output: 299
# Note: N is an integer in the range [0, 10^9].

class Solution:
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        Nlist = list(map(int, str(N)))
        count = 0
        for i in range(len(Nlist)-1):
            if Nlist[i] > Nlist[i+1]:
                Nlist[i-count] -= 1
                for j in range(i-count+1, len(Nlist)):
                    Nlist[j] = 9
                break
            elif Nlist[i] == Nlist[i+1]:
                count += 1
            else:
                count = 0
        return int(''.join(map(str, Nlist)))
