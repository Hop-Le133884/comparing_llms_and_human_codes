
import random

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num
        while left < right:
            mid = (left + right) >> 1
            if mid * mid >= num:
                right = mid
            else:
                left = mid + 1
        return left * left == num

def generate_test_case():
    solution = Solution()

    # Generate a random number
    num = random.randint(1, 10 ** 9)

    # Calculate the expected result using the provided Solution class
    expected_result = solution.isPerfectSquare(num)

    return num, expected_result

def test_generated_test_cases(num_tests):
    test_case_generator_results = []
    for i in range(num_tests):
        num, expected_result = generate_test_case()
        solution = Solution()
        assert solution.isPerfectSquare(num) == expected_result
        print(f"assert solution.isPerfectSquare({num}) == {expected_result}")
        test_case_generator_results.append(f"assert solution.isPerfectSquare({num}) == {expected_result}") # You can find that we construct the test case in the same format as the example
    return test_case_generator_results

if __name__ == "__main__":
    num_tests = 100  # You can change this to generate more test cases
    test_case_generator_results = test_generated_test_cases(num_tests)
