# 217. Contains Duplicate

## Problem Statement

Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

---

## Approach & Thought Process

The most Pythonic and concise solution leverages the properties of a `set`.

A `set` is a collection of **unique** elements. When we convert a list into a set, all duplicate elements are automatically removed.

- Therefore, if the original list `nums` contains duplicates, the resulting set will have **fewer** elements than the list.
- If all elements in the list are unique, the set will have the **same** number of elements.

The implementation simply compares the length of the original list with the length of the set created from it. If `len(nums) != len(set(nums))`, it means duplicates existed, and we correctly return `true`.

---

## Complexity Analysis

- **Time Complexity:** **O(n)**
  - Building a set from an n-element list requires iterating through all the elements once.

- **Space Complexity:** **O(n)**
  - In the worst case (all elements are unique), the new set will store all `n` elements.

## Alternative Approach: HashMap

Another way to solve this problem is by using a hash map (dictionary in Python).  
We iterate through the list and store each number in the hash map as we encounter it.  

- If a number is already present in the hash map, we immediately know it is a duplicate and return `true`.  
- If we finish iterating without finding any duplicates, we return `false`.  

### Implementation

```python
class Solution(object):
    def containsDuplicate(self, nums):
        hashmap = {}
        for num in nums:
            if num in hashmap:
                return True
            hashmap[num] = 1
        return False
