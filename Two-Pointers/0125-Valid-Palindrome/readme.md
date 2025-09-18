# 125. Valid Palindrome

## Problem Statement

Given a string `s`, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases. An empty string is considered a valid palindrome.

---

## Approach & Thought Process

My final and most optimal solution for this problem utilizes the **Two Pointers** technique. This approach is highly efficient as it avoids allocating extra memory. Below, I'll detail this method as well as my initial, more straightforward approach.

### 1. The Optimal Solution: Two Pointers (In-place)

This is the preferred solution in interviews due to its memory efficiency (O(1) space complexity). It works by comparing characters from both ends of the original string, moving inwards.

- **The Logic:**
  1. Initialize two pointers: `left` at the beginning of the string (`0`) and `right` at the end (`len(s) - 1`).
  2. Use a `while` loop that continues as long as `left < right`.
  3. **Inside the loop, we first find the next valid characters:**
     - We move the `left` pointer forward (`left += 1`) until it points to an alphanumeric character.
     - Similarly, we move the `right` pointer backward (`right -= 1`) until it points to an alphanumeric character.
  4. **Compare the characters:**
     - Once both pointers are on valid characters, we compare their lowercase versions.
     - If `s[left].lower() != s[right].lower()`, the string is not a palindrome, and we can immediately `return False`.
  5. **Move pointers inward:**
     - If the characters match, we've confirmed that part of the string is a palindrome. We then move both pointers one step closer to the center (`left += 1`, `right -= 1`) to check the next pair.
  6. If the loop completes without finding any mismatches, it means the entire string is a palindrome, and we `return True`.

- **Complexity Analysis:**
  - **Time Complexity:** O(n), as each pointer traverses each character at most once.
  - **Space Complexity:** **O(1)**, as we only use a few variables for pointers and do not create any new data structures that scale with the input size.

---

## 2. Alternative Approach: Build, Filter, and Reverse

My initial approach to this problem was more direct and involved creating a new, cleaned-up version of the string.

- **The Logic:**
  1. Create a new empty string.
  2. Iterate through the input string `s`. For each character, if it is alphanumeric, convert it to lowercase and append it to the new string.
  3. After the loop, compare the newly created string with its reversed version (`new_string == new_string[::-1]`).

- **Why it's less optimal:** While this solution is correct and easy to understand, its main drawback is its **Space Complexity**. It requires O(n) extra space to store the new string, which can be significant for very large inputs. The Two Pointers method avoids this by performing the check "in-place".