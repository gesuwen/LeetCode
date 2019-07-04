// Array

// Given an unsorted integer array, find the smallest missing positive integer.

// Example 1:

// Input: [1,2,0]
// Output: 3
// Example 2:

// Input: [3,4,-1,1]
// Output: 2
// Example 3:

// Input: [7,8,9,11,12]
// Output: 1
// Note:

// Your algorithm should run in O(n) time and uses constant extra space.

class Solution {
    public int firstMissingPositive(int[] nums) {
        int n = nums.length;
        if (n == 0) return 1;
        int k = partition(nums) + 1;
        int temp = 0;
        int firstMissingIndex = k;
        for (int i = 0; i < k; i++) {
            temp = Math.abs(nums[i]);
            if (temp <= k) {
                nums[temp-1] = (nums[temp-1] < 0) ? nums[temp-1]:-nums[temp-1];
            }
        }
        for (int i = 0; i < k; i++) {
            if (nums[i] > 0) {
                firstMissingIndex = i;
                break;
            }
        }
        return firstMissingIndex + 1;
    }
    
    public int partition(int[] A) {
        int n = A.length;
        int q = -1;
        for (int i = 0; i< n; i++) {
            if (A[i] > 0) {
                q++;
                swap(A, q, i);
            }
        }
        return q;
    }
    
    public void swap(int[] A, int i, int j) {
        if (i != j) {
            A[i] ^= A[j];
            A[j] ^= A[i];
            A[i] ^= A[j];
        }
    }
}