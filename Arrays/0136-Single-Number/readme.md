# 136. Single Number

## Problem Statement

Given a non-empty array of integers `nums`, every element appears twice except for one. Find that single one. You must implement a solution with a linear runtime complexity and use only constant extra space.

---

## Approach & Thought Process

I realized that the bitwise XOR operator would be perfect for this problem.

### The Power of XOR (^)

The XOR operator has two critical properties that make it perfect for this problem:
1.  `A ^ A = 0` (XORing a number with itself results in zero).
2.  `A ^ 0 = A` (XORing a number with zero results in the number itself).

### How XOR Works (Binary Explanation)

The XOR operation works at the binary level. It compares bits one by one: if the bits are the same, the result is 0;
if they are different, the result is 1. Because of this, numbers that appear in pairs completely cancel each other out,
and the unique number remains.

### The Logic

If we take the XOR of all the numbers in the array, every number that appears twice will cancel itself out.

For example, in an array like `[4, 1, 2, 1, 2]`:

The calculation would be `(4 ^ 1 ^ 2 ^ 1 ^ 2)`.
Due to the commutative property of XOR, this is the same as `4 ^ (1 ^ 1) ^ (2 ^ 2)`.

- `1 ^ 1` becomes `0`.
- `2 ^ 2` becomes `0`.

So the expression simplifies to `4 ^ 0 ^ 0`, which is `4`. The single number remains.

By initializing a result variable to 0 and XORing it with every number in the array, we effectively eliminate all the pairs, leaving only the unique number.

---

## Complexity Analysis

- **Time Complexity:** **O(n)**
  - We perform a single pass through the array.

- **Space Complexity:** **O(1)**
  - We only use a single variable (`result`) to store the cumulative XOR value, regardless of the input array's size. No extra data structures are needed.