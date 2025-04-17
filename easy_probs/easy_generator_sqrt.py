
import random

class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left < right:
            mid = (left + right + 1) >> 1
            # mid*mid <= x
            if mid <= x // mid:
                left = mid
            else:
                right = mid - 1
        return left

def generate_test_case():
    solution = Solution()
    
    # Generate a random non-negative integer
    x = random.randint(0, 2**31 - 1)
    
    # Calculate the expected result using the provided Solution class
    expected_result = solution.mySqrt(x)

    return x, expected_result

def test_generated_test_cases(num_tests):
    test_case_generator_results = []
    for i in range(num_tests):
        x, expected_result = generate_test_case()
        solution = Solution()
        assert solution.mySqrt(x) == expected_result
        print(f"assert solution.mySqrt({x}) == {expected_result}")
        test_case_generator_results.append(f"assert solution.mySqrt({x}) == {expected_result}") # You can find that we construct the test case in the same format as the example
    return test_case_generator_results

if __name__ == "__main__":
    num_tests = 100  # You can change this to generate more test cases
    test_case_generator_results = test_generated_test_cases(num_tests)
