
import random

class Solution:
    def findPeakGrid(self, mat):
        l, r = 0, len(mat) - 1
        while l < r:
            mid = (l + r) >> 1
            j = mat[mid].index(max(mat[mid]))
            if mat[mid][j] > mat[mid + 1][j]:
                r = mid
            else:
                l = mid + 1
        return [l, mat[l].index(max(mat[l]))]

def generate_test_case():
    solution = Solution()

    # Generate random m and n
    m = random.randint(1, 11)
    n = random.randint(1, 11)

    # Generate a random matrix
    mat = [[random.randint(1, 100) for _ in range(n)] for _ in range(m)]

    # Calculate the expected result using the provided Solution class
    expected_result = solution.findPeakGrid(mat)

    return mat, expected_result

def test_generated_test_cases(num_tests):
    test_case_generator_results = []
    for i in range(num_tests):
        mat, expected_result = generate_test_case()
        solution = Solution()
        assert solution.findPeakGrid(mat) == expected_result
        print(f"assert solution.findPeakGrid({mat}) == {expected_result}")
        test_case_generator_results.append(f"assert solution.findPeakGrid({mat}) == {expected_result}")
    return test_case_generator_results

if __name__ == "__main__":
    num_tests = 100
    test_case_generator_results = test_generated_test_cases(num_tests)
