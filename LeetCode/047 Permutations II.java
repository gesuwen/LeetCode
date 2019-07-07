// Backtracking

// Given a collection of numbers that might contain duplicates, return all possible unique permutations.

// Example:

// Input: [1,1,2]
// Output:
// [
//   [1,1,2],
//   [1,2,1],
//   [2,1,1]
// ]

class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        Set<List<Integer>> solutions = new HashSet<>();
        permute(nums, 0, new boolean[nums.length], solutions, new ArrayList<>());
        return new ArrayList<>(solutions);
    }
    
    private void permute(int[] array, int index, boolean[] used, Set<List<Integer>> solutions, List<Integer> list) {
        if (index == array.length) {
            solutions.add(new ArrayList<>(list));
            return;
        }
        for (int i = 0; i < array.length; i++) {
            if (used[i] == false) {
                list.add(array[i]);
                used[i] = true;
                permute(array, index + 1, used, solutions, list);
                used[i] = false;
                list.remove(list.size() - 1);
            }
        }
    }
}