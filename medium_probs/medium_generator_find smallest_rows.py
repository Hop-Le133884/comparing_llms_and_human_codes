
import random
from typing import List
from collections import Counter

class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        cnt = Counter()
        for row in mat:
            for x in row:
                cnt[x] += 1
                if cnt[x] == len(mat):
                    return x
        return -1

def generate_test_case():
    solution = Solution()
    
    # Generate random matrix
    m = random.randint(2, 10)
    n = random.randint(2, 10)
    mat = [[random.randint(1, 100) for _ in range(n)] for _ in range(m)]
    
    # Calculate the expected result using the provided Solution class
    expected_result = solution.smallestCommonElement(mat)

    return mat, expected_result

def test_generated_test_cases(num_tests):
    test_case_generator_results = []
    for i in range(num_tests):
        mat, expected_result = generate_test_case()
        solution = Solution()
        assert solution.smallestCommonElement(mat) == expected_result
        print(f"assert solution.smallestCommonElement({mat}) == {expected_result}")
        test_case_generator_results.append(f"assert solution.smallestCommonElement({mat}) == {expected_result}")
    return test_case_generator_results

if __name__ == "__main__":
    num_tests = 100  # You can change this to generate more test cases
    test_case_generator_results = test_generated_test_cases(num_tests)
