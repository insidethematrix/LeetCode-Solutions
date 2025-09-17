# 349. Intersection of Two Arrays

## Problem Statement

Given two integer arrays `nums1` and `nums2`, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

---

## Approach & Thought Process

The most efficient and Pythonic way to find the unique intersection of two arrays is to leverage the `set` data structure.

### The Chosen Solution: Set Intersection Operator

- **The Logic:**
  1. Convert both input lists, `nums1` and `nums2`, into sets. This automatically handles any duplicate elements within each list and prepares them for fast set operations.
  2. Use the `&` operator, which is Python's built-in operator for set intersection. `set1 & set2` will return a new set containing only the elements that are present in **both** `set1` and `set2`.
  3. Since the problem requires the output to be a list, we convert the resulting set back into a list using `list()`.

This approach is highly readable, concise, and leverages the optimized, built-in functionalities of Python.

---

## Alternative Approach: Using One Set and Iteration

Another common way to solve this, without using the `&` operator, is as follows:

- **The Logic:**
  1. Convert the smaller of the two lists into a set to optimize lookups.
  2. Create an empty set to store the intersection results.
  3. Iterate through the second (larger) list. For each element, check if it exists in the set created from the first list.
  4. If it exists, add that element to our result set.
  5. Finally, convert the result set to a list.

This approach is fundamentally the same in terms of complexity but is more explicit in its steps.

---

## Complexity Analysis

- **Time Complexity:** **O(n + m)**
  - Where `n` and `m` are the number of elements in `nums1` and `nums2`, respectively. It takes O(n) to build the first set and O(m) to build the second set. The intersection operation is, on average, very efficient.

- **Space Complexity:** **O(n + m)**
  - In the worst-case scenario, we need to store all unique elements from both lists in the sets.