// Hash Table; Bit Manipulation

// All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

// Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

// Example:

// Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

// Output: ["AAAAACCCCC", "CCCCCAAAAA"]

class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        int L = 10, n = s.length();
        HashSet<String> seen = new HashSet(), output = new HashSet();
        
        for (int start = 0; start < n - L + 1; ++start) {
            String tmp = s.substring(start, start + L);
            if (seen.contains(tmp)) output.add(tmp);
            seen.add(tmp);
        }
        return new ArrayList<String>(output);
    }
}