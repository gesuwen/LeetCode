# Dynamic Programming

# You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
#
# Example 1:
#
# Input: coins = [1, 2, 5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:
#
# Input: coins = [2], amount = 3
# Output: -1
# Note:
# You may assume that you have an infinite number of each kind of coin.

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 1: return 0
        return self.coinChangeDP(coins, amount, [0] * amount)

    def coinChangeDP(self, coins, rem, count):
        if rem < 0: return -1
        if rem == 0: return 0
        if count[rem - 1] != 0: return count[rem - 1]
        minChange = float("Inf")
        for coin in coins:
            res = self.coinChangeDP(coins, rem - coin, count)
            if res >= 0 and res < minChange:
                minChange = res + 1
        if minChange == float("Inf"):
            count[rem-1] = -1
        else:
            count[rem-1] = minChange
        return count[rem - 1]
