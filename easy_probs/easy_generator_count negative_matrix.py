
import random
from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        i, j = m - 1, 0
        ans = 0
        while i >= 0 and j < n:
            if grid[i][j] < 0:
                ans += n - j
                i -= 1
            else:
                j += 1
        return ans

def generate_test_case() -> (List[List[int]], int):
    solution = Solution()
    
    # Generate random m and n values
    m = random.randint(1, 11)
    n = random.randint(1, 11)
    
    # Generate random grid with m x n size
    grid = []
    for _ in range(m):
        row = []
        for _ in range(n):
            row.append(random.randint(-100, 100))
        grid.append(row)
    
    # Calculate the expected result using the provided Solution class
    expected_result = solution.countNegatives(grid)

    return grid, expected_result

def test_generated_test_cases(num_tests):
    solution = Solution()
    test_case_generator_results = []
    for i in range(num_tests):
        grid, expected_result = generate_test_case()
        assert solution.countNegatives(grid) == expected_result
        print(f"assert solution.countNegatives({grid}) == {expected_result}")
        test_case_generator_results.append(f"assert solution.countNegatives({grid}) == {expected_result}") # You can find that we construct the test case in the same format as the example
    return test_case_generator_results

if __name__ == "__main__":
    num_tests = 100  # You can change this to generate more test cases
    test_case_generator_results = test_generated_test_cases(num_tests)
