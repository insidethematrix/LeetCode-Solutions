class Solution(object):
    def isAnagram(self, s, t):
        """
        Checks if string t is an anagram of string s using a single
        frequency map for optimal memory usage.
        """
        # If the lengths are different, they cannot be anagrams.
        # This is the quickest check to fail fast.
        if len(s) != len(t):
            return False

        # Build the frequency map for string s.
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1

        # Decrement the counters in the map using the characters from string t.
        for char in t:
            # If a character from t is not in our map or its count is already zero,
            # it means t has an extra character or a higher frequency of a character.
            # Thus, it cannot be an anagram.
            if char not in counts or counts[char] == 0:
                return False
            counts[char] -= 1

        # If the loop completes successfully, it means all characters and their
        # frequencies matched perfectly.
        return True