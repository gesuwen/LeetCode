// Array; Backtracking
//
// Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
//
// Note: The solution set must not contain duplicate subsets.
//
// Example:
//
// Input: [1,2,2]
// Output:
// [
//   [2],
//   [1],
//   [1,2,2],
//   [2,2],
//   [1,2],
//   []
// ]

class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        subsetWithDupHelper(nums, 0, res, new ArrayList<>());
        return res;
    }

    private void subsetWithDupHelper(int[] nums, int pos, List<List<Integer>> res, List<Integer> tmpRes) {
        if (pos <= nums.length) res.add(new ArrayList<>(tmpRes));
        for (int i = pos; i < nums.length; i++) {
            if (i > pos && nums[i] == nums[i-1]) continue;
            tmpRes.add(nums[i]);
            subsetWithDupHelper(nums, i+1, res, tmpRes);
            tmpRes.remove(tmpRes.size()-1);
        }
    }
}
