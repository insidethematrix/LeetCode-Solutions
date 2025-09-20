# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution(object):
    def twoSum(self, numbers, target):
        """
        Finds two numbers in a sorted array that add up to the target
        using the Two Pointers technique for O(1) space complexity.
        """
        left, right = 0, len(numbers) - 1

        # The loop continues as long as the two pointers have not crossed.
        while left < right:
            # Calculate the sum once per iteration.
            current_sum = numbers[left] + numbers[right]

            # If we found the target, return the 1-indexed positions.
            if current_sum == target:
                return [left + 1, right + 1]
            
            # If the sum is too large, we need to decrease it by moving the right pointer.
            elif current_sum > target:
                right -= 1
            
            # If the sum is too small, we need to increase it by moving the left pointer.
            else: # current_sum < target
                left += 1