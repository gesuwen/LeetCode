# Map

# Alice has a hand of cards, given as an array of integers.
#
# Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.
#
# Return true if and only if she can.
#
#
#
# Example 1:
#
# Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].
# Example 2:
#
# Input: hand = [1,2,3,4,5], W = 4
# Output: false
# Explanation: Alice's hand can't be rearranged into groups of 4.
#
#
# Note:
#
# 1 <= hand.length <= 10000
# 0 <= hand[i] <= 10^9
# 1 <= W <= hand.length

class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        # Solution 1
        handDict = collections.Counter(hand)
        while handDict:
            first = min(handDict)
            for i in range(first, first+W):
                curr = handDict[i]
                if not curr:
                    return False
                if curr == 1:
                    del handDict[i]
                else:
                    handDict[i] = curr - 1
        return True

        # Solution 2

        # hand = sorted(hand)
        # while len(hand) > 0:
        #     first = hand[0]
        #     for i in range(W):
        #         if first+i in hand:
        #             hand.remove(first+i)
        #         else:
        #             return False
        # return True
