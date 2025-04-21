# easy_fixedPoint.py

class LLM_Solution:
    def fixedPoint(self, arr: list[int]) -> int:
        """
        Given an array of distinct integers arr, where arr is sorted in ascending order,
        return the smallest index i that satisfies arr[i] == i.
        If there is no such index, return -1.
        """

        for i in range(len(arr)):
            if arr[i] == i:
                return i

        return -1