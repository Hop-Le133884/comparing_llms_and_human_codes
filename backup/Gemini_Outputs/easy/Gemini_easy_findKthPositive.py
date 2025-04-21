# easy_findKthPositive.py

class LLM_Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        """
        Given an array arr of positive integers sorted in strictly increasing order,
        and an integer k. Return the kth positive integer that is missing from arr.
        """

        missing_count = 0
        possible_positive = 1
        arr_index = 0

        while missing_count < k:
            if arr_index < len(arr) and arr[arr_index] == possible_positive:
                possible_positive += 1
                arr_index += 1
            else:
                missing_count += 1
                possible_positive += 1

        return possible_positive - 1