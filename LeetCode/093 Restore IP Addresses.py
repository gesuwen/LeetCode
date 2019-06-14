# String; Backtracking

# Given a string containing only digits, restore it by returning all possible valid IP address combinations.
#
# Example:
#
# Input: "25525511135"
# Output: ["255.255.11.135", "255.255.111.35"]

class Solution:
    def dfs(self, s, path, res):
        if len(s) > (4 - len(path)) * 3:
            return
        if not s and len(path) == 4:
            res.append(".".join(path))
        for i in range(1, 4):
            if i <= len(s):
                number = int(s[:i])
                if str(number)==s[:i] and number < 256:
                    self.dfs(s[i:], path+[s[:i]], res)

    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:
            return []
        res = []
        self.dfs(s, [], res)
        return res
