// String; Dynamic Programming
//
// Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.
//
// Below is one possible representation of s1 = "great":
//
//     great
//    /    \
//   gr    eat
//  / \    /  \
// g   r  e   at
//            / \
//           a   t
// To scramble the string, we may choose any non-leaf node and swap its two children.
//
// For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".
//
//     rgeat
//    /    \
//   rg    eat
//  / \    /  \
// r   g  e   at
//            / \
//           a   t
// We say that "rgeat" is a scrambled string of "great".
//
// Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".
//
//     rgtae
//    /    \
//   rg    tae
//  / \    /  \
// r   g  ta  e
//        / \
//       t   a
// We say that "rgtae" is a scrambled string of "great".
//
// Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
//
// Example 1:
//
// Input: s1 = "great", s2 = "rgeat"
// Output: true
// Example 2:
//
// Input: s1 = "abcde", s2 = "caebd"
// Output: false

class Solution {
    public boolean isScramble(String s1, String s2) {
        if (s1.length() != s2.length()) return false;
        int len = s1.length();

        boolean[][][] F = new boolean[len][len][len+1];
        for (int k = 1; k <= len; k++) {
            for (int i = 0; i + k <= len; i++) {
                for (int j = 0; j + k <= len; j++) {
                    if (k == 1) F[i][j][k] = s1.charAt(i) == s2.charAt(j);
                    else for (int q = 1; q < k && !F[i][j][k]; q++) {
                        F[i][j][k] = (F[i][j][q] && F[i+q][j+q][k-q]) || (F[i][j+k-q][q] && F[i+q][j][k-q]);
                    }
                }
            }
        }
        return F[0][0][len];
    }
}
