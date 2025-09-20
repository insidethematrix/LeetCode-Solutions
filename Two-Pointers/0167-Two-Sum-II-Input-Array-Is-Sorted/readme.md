# 167. Two Sum II - Input Array Is Sorted

## Problem Statement

Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific `target` number. Return the indices of the two numbers (1-indexed) as an integer array of size 2.

---

## Approach & Thought Process

The key to this problem is the detail that the input array is **sorted**. This allows for a highly efficient solution using the **Two Pointers** technique, which is a significant improvement over the standard Hash Map approach used for the unsorted version of "Two Sum".

### 1. The Optimal Solution: Two Pointers

This approach achieves the solution with constant extra space, making it the ideal choice.

- **The Logic:**
  1. Initialize two pointers: `left` at the beginning of the array (`index 0`) and `right` at the end (`len(numbers) - 1`).
  2. Use a `while` loop that continues as long as `left` is less than `right`.
  3. Inside the loop, calculate the sum of the values at the two pointers: `current_sum = numbers[left] + numbers[right]`.
  4. **Compare the sum with the target:**
     - If `current_sum > target`, it means our sum is too large. Since the array is sorted, we must decrease the sum. We do this by moving the `right` pointer one step to the left (`right -= 1`), effectively picking a smaller number.
     - If `current_sum < target`, our sum is too small. We need to increase it by moving the `left` pointer one step to the right (`left += 1`), picking a larger number.
     - If `current_sum == target`, we have found our pair. We can immediately return their 1-indexed positions: `[left + 1, right + 1]`.

- **Complexity Analysis:**
  - **Time Complexity:** O(n), as the two pointers will together traverse the entire array at most once.
  - **Space Complexity:** **O(1)**. This is the main advantage. We are not using any extra space that scales with the size of the input.

---

## 2. Alternative Approach: Hash Map

For comparison, if the array were **not sorted**, the standard solution would be to use a Hash Map. I initially implemented this as well.

- **The Logic:**
  1. Iterate through the array.
  2. For each number, calculate its complement (`diff = target - number`).
  3. Check if this `diff` already exists in the hash map. If it does, we have found our pair.
  4. If not, store the current number and its index in the hash map.
- **Why it's less optimal for *this* problem:** While its time complexity is also O(n), its space complexity is **O(n)** due to the hash map. The Two Pointers approach leverages the "sorted" property to avoid this extra space cost.