class LLM_Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        Search a 2D Matrix

        You are given an m x n integer matrix matrix with the following two properties:
        - Each row is sorted in non-decreasing order.
        - The first integer of each row is greater than the last integer of the previous row.
        Given an integer target, return true if target is in matrix or false otherwise.
        You must write a solution in O(log(m * n)) time complexity.
        """
        if not matrix:
            return False

        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            mid = (left + right) // 2
            mid_value = matrix[mid // cols][mid % cols]

            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False