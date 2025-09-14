# 1. Two Sum

## Problem Statement


Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

---

## Approach & Thought Process

This section explains the journey from a naive solution to an optimal one.

### 1. Brute Force Approach

The most straightforward solution that comes to mind is to check every possible pair of numbers in the array.

- **The Logic:** Use two nested loops. The outer loop picks an element, and the inner loop iterates through the rest of the array to find a second element that sums up to the target.
- **Drawback:** The time complexity of this approach is **O(n²)**. For a large input array, this would be too slow and likely result in a "Time Limit Exceeded" error on LeetCode. This clearly indicates the need for a more efficient approach.

### 2. Optimized Solution: Using a Hash Map

To achieve a better time complexity, I aimed for a solution that would only require one pass through the array, making it O(n). The perfect data structure for this task is a Hash Map (a `dictionary` in Python).

- **The Logic:**
  1. Create an empty hash map, let's call it `hashmap`, to store the numbers we've seen so far and their indices (e.g., `{value: index}`).
  2. Iterate through the `nums` array with access to both the index (`i`) and the value (`n`).
  3. For each element, calculate the required complement: `diff = target - n`.
  4. Check if this `diff` exists as a key in our `hashmap`.
     - If it exists, we have found our pair. We can immediately return the index of the `diff` from the map (`hashmap[diff]`) and the index of the current element (`i`).
     - If it does not exist, add the current number `n` and its index `i` to the `hashmap`. This prepares the map for future checks.

This approach trades a small amount of space (for the hash map) for a significant gain in time efficiency.

---

## Complexity Analysis

This analysis is for the final, optimized solution.

- **Time Complexity:** **O(n)**
  - We iterate through the `nums` array only once. The hash map lookups and insertions are, on average, O(1) operations.

- **Space Complexity:** **O(n)**
  - In the worst-case scenario, we might have to store all `n` elements of the array in the hash map (e.g., if the pair is found at the very end or not at all).