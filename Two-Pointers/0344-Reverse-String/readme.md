# 344. Reverse String

## Problem Statement

Write a function that reverses a string. The input string is given as an array of characters `s`. You must do this by modifying the input array in-place with O(1) extra memory.

---

## Approach: Two Pointers

The most efficient way to reverse an array in-place is by using the **Two Pointers** technique.

- **The Logic:**
  1. Initialize two pointers: `left` at the beginning of the array (`0`) and `right` at the end (`len(s) - 1`).
  2. Use a `while` loop that continues as long as the `left` pointer is to the left of the `right` pointer (`left < right`).
  3. **Inside the loop, swap the elements:** We swap the character at the `left` pointer with the character at the `right` pointer. In Python, this can be done elegantly in one line: `s[left], s[right] = s[right], s[left]`.
  4. **Move the pointers inward:** After the swap, we move both pointers one step closer to the center of the array (`left += 1`, `right -= 1`).
  5. The loop terminates when the pointers meet or cross, at which point the entire array has been reversed.

- **Complexity Analysis:**
  - **Time Complexity:** **O(n)**, as we iterate through roughly half of the array.
  - **Space Complexity:** **O(1)**, because the reversal is done in-place, without allocating any extra memory that scales with the input size.