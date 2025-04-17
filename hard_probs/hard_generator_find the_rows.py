

import random
from typing import List

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        pre = [0]
        for cur in mat:
            pre = sorted(a + b for a in pre for b in cur[:k])[:k]
        return pre[-1]


def generate_test_case():
    solution = Solution()
    
    # Generate random matrix of numbers
    m = random.randint(2, 6)
    n = random.randint(2, 6)
    mat = []
    for _ in range(m):
        row = random.sample(range(1, 101), n)
        row.sort()
        mat.append(row)

    # Generate a random k value
    k = random.randint(1, min(200, n**m))

    # Calculate the expected result using the provided Solution class
    expected_result = solution.kthSmallest(mat, k)

    return mat, k, expected_result


def test_generated_test_cases(num_tests):
    test_case_generator_results = []
    for i in range(num_tests):
        mat, k, expected_result = generate_test_case()
        solution = Solution()
        assert solution.kthSmallest(mat, k) == expected_result
        test_case = f"assert solution.kthSmallest({mat}, {k}) == {expected_result}"
        print(test_case)
        test_case_generator_results.append(test_case)
    return test_case_generator_results


if __name__ == "__main__":
    num_tests = 100  # You can change this to generate more test cases
    test_case_generator_results = test_generated_test_cases(num_tests)

