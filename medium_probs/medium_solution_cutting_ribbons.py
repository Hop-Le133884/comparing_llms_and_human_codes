
import random
from typing import List
from collections import namedtuple

TestCase = namedtuple("TestCase", ["ribbons", "k", "expected_result"])

def generate_test_case() -> TestCase:
    solution = Solution()
    
    # Generate random ribbons list
    ribbons = random.sample(range(1, 101), random.randint(2, 10))
    
    # Generate a random k value
    k = random.randint(1, 100)

    # Calculate the expected result using the provided Solution class
    expected_result = solution.maxLength(ribbons, k)

    return TestCase(ribbons, k, expected_result)

def test_generated_test_cases(num_tests: int) -> List[str]:
    test_case_generator_results = []
    for i in range(num_tests):
        test_case = generate_test_case()
        assert_solution = f"assert solution.maxLength({test_case.ribbons}, {test_case.k}) == {test_case.expected_result}"
        test_case_generator_results.append(assert_solution)
    return test_case_generator_results

if __name__ == "__main__":
    num_tests = 100 # You can change this to generate more test cases
    test_case_generator_results = test_generated_test_cases(num_tests)
