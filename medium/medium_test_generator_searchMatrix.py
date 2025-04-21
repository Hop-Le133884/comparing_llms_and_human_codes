import time

from typing import List

import random
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left < right:
            mid = (left + right) >> 1
            x, y = divmod(mid, n)
            if matrix[x][y] >= target:
                right = mid
            else:
                left = mid + 1
        return matrix[left // n][left % n] == target

def generate_test_case():

    solution = Solution()

    

    # Generate random dimensions for the matrix

    m = random.randint(1, 100)

    n = random.randint(1, 100)

    

    # Generate a random matrix (sorted row-wise)

    matrix = []

    for i in range(m):

        row = sorted([random.randint(-10000, 10000) for _ in range(n)])

        matrix.append(row)

    

    # Generate a random target number

    target = random.randint(-10000, 10000)

    # Calculate the expected result using the provided Solution class

    expected_result = solution.searchMatrix(matrix, target)

    return matrix, target, expected_result

def test_generated_test_cases(num_tests):

    test_case_generator_results = []

    for i in range(num_tests):

        matrix, target, expected_result = generate_test_case()

        solution = Solution()

        assert solution.searchMatrix(matrix, target) == expected_result


        test_case_generator_results.append(f"assert solution.searchMatrix({matrix}, {target}) == {expected_result}")

    return (matrix,target), test_case_generator_results

if __name__ == "__main__":

    num_tests = 100  # You can change this to generate more test cases

    test_case_generator_results = test_generated_test_cases(num_tests, Solution())
