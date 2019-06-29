// Array; Two Pointers

// Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

// Example:

// Given array nums = [-1, 2, 1, -4], and target = 1.

// The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int res = nums[0] + nums[1] + nums[nums.length-1];
        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 2; i++) {
            int start = i + 1, end = nums.length - 1;
            while (start < end) {
                int curr = nums[i] + nums[start] + nums[end];
                if (Math.abs(curr - target) < Math.abs(res - target)) res = curr;
                if (curr < target) start++;
                else end--;
            }
        }
        return res;
    }
}