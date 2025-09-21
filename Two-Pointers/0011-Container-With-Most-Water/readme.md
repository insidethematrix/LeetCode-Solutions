# 11. Container With Most Water

## Problem Statement

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i-th` line are `(i, 0)` and `(i, height[i])`. Find two lines that together with the x-axis form a container, such that the container contains the most water. Return the maximum amount of water a container can store.

---

## Approach & Thought Process

A brute-force approach checking every pair of lines would be O(n²), which is too slow. A far more efficient O(n) solution can be achieved using the **Two Pointers** technique.

### The Two Pointers Solution

The core idea is to start with the widest possible container and iteratively narrow it down, intelligently seeking a larger area by making a "greedy" choice at each step.

- **The Logic:**
  1. Initialize two pointers: `left` at the beginning of the array (`0`) and `right` at the end (`len(height) - 1`). This represents the widest container. Also, initialize a `max_area` variable to `0`.
  2. Use a `while` loop that continues as long as `left < right`.
  3. **Inside the loop, calculate the current area:**
     - The width is simply `right - left`.
     - The water level is limited by the shorter of the two lines, so the height is `min(height[left], height[right])`.
     - The current area is `width * height`. We update `max_area` with this value if it's larger than the previous max.
  4. **The Critical Decision: Which Pointer to Move?**
     - Our goal is to maximize the area (`width * height`).
     - In every step, we are forced to decrease the `width`. Therefore, the **only way** to potentially find a larger area is to find a **taller height**.
     - The current height is limited by the shorter of the two lines.
       - If we move the pointer of the *taller* line inward, the best we can do is find a new line that is just as tall, but the height will still be limited by the original shorter line. We are guaranteed to have a smaller or equal area.
       - However, if we move the pointer of the **shorter** line inward, we give ourselves a chance to find a new, taller line that could potentially increase the overall height and offset the decrease in width.
     - This greedy choice—always moving the pointer of the shorter line—ensures that we never miss the optimal solution.
  5. The loop continues until the pointers cross, by which time we have explored all promising configurations.

- **Complexity Analysis:**
  - **Time Complexity:** **O(n)**, as the `left` and `right` pointers will each traverse the array at most once.
  - **Space Complexity:** **O(1)**, using only a few variables for pointers and tracking the maximum area.