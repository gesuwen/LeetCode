// Array; Hash Table; Two Pointers

// Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

// Note:

// The solution set must not contain duplicate quadruplets.

// Example:

// Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

// A solution set is:
// [
//   [-1,  0, 0, 1],
//   [-2, -1, 1, 2],
//   [-2,  0, 0, 2]
// ]

class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        ArrayList<List<Integer>> res = new ArrayList<List<Integer>>();
        int len = nums.length;
        if (nums == null || len < 4) return res;
        Arrays.sort(nums);
        int max = nums[len - 1];
        if (4 * nums[0] > target || 4 * max < target) return res;
        int i, z;
        for (i = 0; i < len; i++) {
            z = nums[i];
            if (i > 0 && z == nums[i-1]) continue;
            if (z + 3 * max < target) continue;
            if (4 * z > target) break;
            if (4 * z == target) {
                if (i + 3 < len && nums[i+3] == z) {
                    res.add(Arrays.asList(z, z, z, z));
                }
                break;
            }
            threeSum(nums, target-z, i+1, len-1, res, z);
        }
        return res;
    }
    
    public void threeSum(int[] nums, int target, int low, int high, ArrayList<List<Integer>> fourSumList, int z1) {
        if (low + 1 >= high) return;
        int max = nums[high];
        if (3 * nums[low] > target || 3 * max < target) return;
        int i, z;
        for (i = low; i < high - 1; i++) {
            z = nums[i];
            if (i > low && z == nums[i - 1]) continue;
            if (z + 2 * max < target) continue;
            if (3 * z > target) break;
            if (3 * z == target) {
                if (i + 1 < high && nums[i + 2] == z) fourSumList.add(Arrays.asList(z1, z, z, z));
                break;
            }
            twoSum(nums, target - z, i + 1, high, fourSumList, z1, z);
        }
    }
    
    public void twoSum(int[] nums, int target, int low, int high, ArrayList<List<Integer>> fourSumList, int z1, int z2) {
        if (low >= high) return;
        if (2 * nums[low] > target || 2 * nums[high] < target) return;
        int i = low, j = high, sum, x;
        while (i < j) {
            sum = nums[i] + nums[j];
            if (sum == target) {
                fourSumList.add(Arrays.asList(z1, z2, nums[i], nums[j]));
                x = nums[i];
                while (++i < j && nums[i] == x);
                x = nums[j];
                while (--j > i && nums[j] == x);
            }
            else if (sum < target) i++;
            else j--;
        }
        return;
    }
}