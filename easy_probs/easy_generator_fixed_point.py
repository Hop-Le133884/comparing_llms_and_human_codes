
import random

class Solution:
    def fixedPoint(self, arr):
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) >> 1
            if arr[mid] >= mid:
                right = mid
            else:
                left = mid + 1
        return left if arr[left] == left else -1

def generate_test_case():
    solution = Solution()
    
    # Generate random numbers list
    arr = random.sample(range(-10**9, 10**9+1), random.randint(1, 10001))
    
    # Calculate the expected result using the provided Solution class
    expected_result = solution.fixedPoint(arr)

    return arr, expected_result

def test_generated_test_cases(num_tests):
    test_case_generator_results = []
    for i in range(num_tests):
        arr, expected_result = generate_test_case()
        solution = Solution()
        assert solution.fixedPoint(arr) == expected_result
        print(f"assert solution.fixedPoint({arr}) == {expected_result}")
        test_case_generator_results.append(f"assert solution.fixedPoint({arr}) == {expected_result}")
    return test_case_generator_results

if __name__ == "__main__":
    num_tests = 100  # You can change this to generate more test cases
    test_case_generator_results = test_generated_test_cases(num_tests)
