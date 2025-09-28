# 643. Maximum Average Subarray I

## Problem Statement

You are given an integer array `nums` consisting of `n` elements, and an integer `k`. Find a contiguous subarray whose length is equal to `k` that has the maximum average value and return this value.

---

## Approach: Fixed-Size Sliding Window

This problem is a classic example of the **Fixed-Size Sliding Window** technique. A brute-force approach would be to calculate the sum of every possible subarray of length `k`, which would be too slow (O(n*k)). The sliding window pattern optimizes this to a single pass, O(n).

- **The Logic:**
  1. **Initialize the Window:** First, we calculate the sum of the initial `k` elements. This sum is our starting `current_sum` and also our initial `max_sum`.
  2. **Slide the Window:** We then iterate through the rest of the array, starting from the `k-th` index. In each iteration, we "slide" our window one step to the right.
  3. **Efficient Sum Update:** Instead of re-calculating the sum of the new window from scratch, we update the `current_sum` in O(1) time. We do this by:
     - **Adding** the new element that just entered the window (`nums[i]`).
     - **Subtracting** the old element that just left the window (`nums[i-k]`).
  4. **Track the Maximum:** After each slide, we compare the `current_sum` with our `max_sum` and update `max_sum` if the new sum is larger.
  5. **Calculate the Average:** After the loop finishes, `max_sum` will hold the maximum sum found among all subarrays of length `k`. The final step is to divide this sum by `k` to get the maximum average.

- **Complexity Analysis:**
  - **Time Complexity:** **O(n)**. We iterate through the `nums` array only once.
  - **Space Complexity:** **O(1)**. We only use a few variables to store the sums and pointers, regardless of the input size.