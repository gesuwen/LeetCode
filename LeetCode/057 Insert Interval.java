// Array; Sort 

// Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

// You may assume that the intervals were initially sorted according to their start times.

// Example 1:

// Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
// Output: [[1,5],[6,9]]
// Example 2:

// Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
// Output: [[1,2],[3,10],[12,16]]
// Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
// NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        if (newInterval.length == 0) return intervals;
        List<int[]> results = new ArrayList<int[]>();
        int index = 0;
        for (int[] interval : intervals) {
            int[] result = new int[2];
            if (interval[1] < newInterval[0]) {
                results.add(interval);
                index++;
            }
            else if (interval[0] > newInterval[1]) {
                results.add(interval);
            }
            else {
                newInterval[0] = interval[0] < newInterval[0] ? interval[0] : newInterval[0];
                newInterval[1] = interval[1] > newInterval[1] ? interval[1] : newInterval[1];
            }
        }
        results.add(index, newInterval);
        int[][] finalResults = new int[results.size()][2];
        int i = 0;
        for (int[] result : results) {
            finalResults[i++] = result;
        }
        return finalResults;
    }
}