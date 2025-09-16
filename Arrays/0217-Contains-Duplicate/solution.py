class Solution(object):
    def containsDuplicate(self, nums):
        # Convert list to a set, which automatically removes duplicates
        # If the length changes, it means there were duplicates
        return len(nums) != len(set(nums)) 

