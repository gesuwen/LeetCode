// String; Dynamic Programming; Backtracking; Greedy

// Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

// '?' Matches any single character.
// '*' Matches any sequence of characters (including the empty sequence).
// The matching should cover the entire input string (not partial).

// Note:

// s could be empty and contains only lowercase letters a-z.
// p could be empty and contains only lowercase letters a-z, and characters like ? or *.
// Example 1:

// Input:
// s = "aa"
// p = "a"
// Output: false
// Explanation: "a" does not match the entire string "aa".
// Example 2:

// Input:
// s = "aa"
// p = "*"
// Output: true
// Explanation: '*' matches any sequence.
// Example 3:

// Input:
// s = "cb"
// p = "?a"
// Output: false
// Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
// Example 4:

// Input:
// s = "adceb"
// p = "*a*b"
// Output: true
// Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
// Example 5:

// Input:
// s = "acdcb"
// p = "a*c?b"
// Output: false

class Solution {
    public boolean isMatch(String str, String pattern) {
        int s = 0, p = 0, match = 0, startIdx = -1;
        while (s < str.length()) {
            if (p < pattern.length() && (pattern.charAt(p) == '?' || str.charAt(s) == pattern.charAt(p))) {
                s++;
                p++;
            }
            else if (p < pattern.length() && pattern.charAt(p) == '*') {
                startIdx = p;
                match = s;
                p++;
            }
            else if (startIdx != -1) {
                p = startIdx + 1;
                match++;
                s = match;
            }
            else return false;
        }
        while (p < pattern.length() && pattern.charAt(p) == '*')
            p++;
        return p == pattern.length();
    }
}