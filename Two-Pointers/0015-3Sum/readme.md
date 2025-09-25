# 15. 3Sum

## Problem Statement

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`. Notice that the solution set must not contain duplicate triplets.

---

## Approach & Thought Process

A brute-force solution with three nested loops would be O(n³), which is too slow. The key to an optimal O(n²) solution is to **sort the array first** and then use a modified **Two Pointers** approach.

This problem can be broken down into a `Two Sum II` problem within a loop.

- **The Logic:**
  1. **Sort the Array:** First, sort the input array `nums`. This is crucial as it allows us to use the Two Pointers technique and easily handle duplicates.
  2. **Main Loop:** Iterate through the sorted array with a `for` loop. The current element `nums[i]` (let's call it `a`) will be the first of our potential three numbers.
  3. **Handling Duplicates (Outer Loop):** To avoid duplicate triplets, we must ensure that we don't use the same starting element `a` more than once. We do this by checking if the current element is the same as the previous one (`if i > 0 and a == nums[i-1]`). If it is, we `continue` to the next iteration.
  4. **The `Two Sum II` Sub-Problem:** For each element `a`, our goal is to find two other numbers in the rest of the array (`from i+1 to the end`) that sum up to `-a`. This is exactly the "Two Sum II" problem.
     - We initialize a `left` pointer at `i + 1` and a `right` pointer at the end of the array.
  5. **Two Pointers Logic:**
     - While `left < right`, we calculate `threeSum = a + nums[left] + nums[right]`.
     - If `threeSum > 0`, we need a smaller sum, so we move the `right` pointer to the left (`right -= 1`).
     - If `threeSum < 0`, we need a larger sum, so we move the `left` pointer to the right (`left += 1`).
     - If `threeSum == 0`, we've found a valid triplet. We add it to our result list.
  6. **Handling Duplicates (Inner Loop):** After finding a valid triplet, we must move our pointers to avoid finding the *same* triplet again. We increment `left` and then use a `while` loop to skip over any subsequent identical elements (`while nums[left] == nums[left - 1] and left < right`). This ensures that our `left` pointer always moves to a new, unique value for the next check.

- **Complexity Analysis:**
  - **Time Complexity:** **O(n²)**. The initial sort takes O(n log n). The main `for` loop runs `n` times, and the `while` loop (Two Pointers) inside it takes O(n) time in the worst case. This gives us O(n log n + n²), which simplifies to O(n²).
  - **Space Complexity:** O(1) or O(n), depending on the implementation of the sorting algorithm used. If we don't count the space used for the output `result` list, the space complexity is constant as we only use a few variables.