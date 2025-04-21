# easy_nextGreatestLetter.py

class LLM_Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        """
        Given an array of characters letters that is sorted in non-decreasing order, and a character target,
        return the smallest character in letters that is lexicographically greater than target.
        If such a character does not exist, return the first character in letters.
        """

        for letter in letters:
            if letter > target:
                return letter

        return letters[0]