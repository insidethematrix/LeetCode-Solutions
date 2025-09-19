# 242. Valid Anagram

## Problem Statement

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

---

## Approach & Thought Process

My initial and a very clear approach to this problem is to count the frequency of each character in both strings and then compare the frequency maps.

### 1. The Two Hash Maps Approach (My Solution)

This method is straightforward and relies on the definition of an anagram: if two strings are anagrams, they must contain the exact same characters with the exact same frequencies.

- **The Logic:**
  1. Create two empty hash maps (dictionaries), `freq1` for string `s` and `freq2` for string `t`.
  2. Iterate through string `s`. For each character, increment its count in `freq1`.
  3. Iterate through string `t`. For each character, increment its count in `freq2`.
  4. Finally, compare the two hash maps. In Python, `freq1 == freq2` will return `true` only if both dictionaries have the same keys with the same corresponding values. This directly tells us if the strings are anagrams.

- **Complexity Analysis:**
  - **Time Complexity:** O(s + t), because we need to iterate through both strings once to build the maps.
  - **Space Complexity:** O(s + t) in the worst case, as we store character counts for both strings. (More accurately, O(k) where k is the number of unique characters, which is constant for ASCII, so it can be considered O(1)).

---

## Alternative and More Optimized Approaches

While my solution is correct, there are other common and sometimes more concise ways to solve this.

### 2. The Single Hash Map Approach

A slightly more memory-efficient approach uses only one hash map.

- **The Logic:**
  1. First, check if the lengths of `s` and `t` are different. If so, they can't be anagrams, so return `false`.
  2. Build a frequency map for string `s` only.
  3. Iterate through string `t`. For each character in `t`, decrement its count in the map.
  4. If at any point a character from `t` is not in the map, or its count is already zero, return `false`.
  5. If the loop completes, it means all character counts matched perfectly.

### 3. The Sorting Approach

A very simple, though often less time-efficient, solution is to sort both strings.

- **The Logic:** If two strings are anagrams, their sorted versions will be identical.
- **Implementation:** `return sorted(s) == sorted(t)`
- **Drawback:** The time complexity is dominated by the sorting algorithm, which is typically **O(n log n)**, making it slower than the O(n) hash map approach for large strings.

### 4. The Most Pythonic Way: `collections.Counter`

Python's standard library offers a specialized dictionary for counting, which makes the hash map approach incredibly clean.

- **The Logic:** `collections.Counter` does exactly what we did manually: it builds a frequency map. We can then compare the two counters.
- **Implementation:** `return collections.Counter(s) == collections.Counter(t)`